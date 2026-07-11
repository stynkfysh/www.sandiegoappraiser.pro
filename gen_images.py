#!/usr/bin/env python3
import os, json, base64, time, io, sys, urllib.request
from PIL import Image
# ================= Gemini image generator (localized for sandiegoappraiser.pro) =================
# Resumable: pass a per-call time budget in seconds as argv[1] (e.g. 38) and
# re-invoke until it prints missing_tasks=0 — background procs don't persist.
# ===================================================================================================

HERE=os.path.dirname(os.path.abspath(__file__))
_KEY_CANDIDATES=[
    "/Users/brianward/Library/Mobile Documents/com~apple~CloudDocs/Reports/_Claude/gemini-api-key.txt",
    "/sessions/admiring-vigilant-goodall/mnt/Reports/_Claude/gemini-api-key.txt",
]
KEY=None
for _p in _KEY_CANDIDATES:
    if os.path.isfile(_p):
        KEY=open(_p).read().strip(); break
if KEY is None:
    raise FileNotFoundError("gemini-api-key.txt not found in any candidate path")
DST=HERE
URL=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent?key={KEY}"
LOG=open(os.path.join(HERE,"gen_progress.log"),"a",buffering=1)
def log(*a): print(*a,file=LOG); print(*a)

STYLE=" Photorealistic, professional real-estate marketing photography, natural daylight, high detail, no people in the foreground, no text, no watermark, no logos, no signage lettering."

def gen(prompt, tries=4):
    body=json.dumps({"contents":[{"parts":[{"text":prompt+STYLE}]}],
                     "generationConfig":{"responseModalities":["IMAGE"]}}).encode()
    for t in range(tries):
        try:
            req=urllib.request.Request(URL,data=body,headers={"Content-Type":"application/json"})
            r=urllib.request.urlopen(req,timeout=120)
            d=json.loads(r.read())
            for p in d["candidates"][0]["content"]["parts"]:
                k="inlineData" if "inlineData" in p else ("inline_data" if "inline_data" in p else None)
                if k: return base64.b64decode(p[k]["data"])
            log("  no image part, retry",t)
        except Exception as e:
            log("  err",t,str(e)[:120]); time.sleep(4+3*t)
    return None

def save(raw, targets, w, h=None, q=82):
    im=Image.open(io.BytesIO(raw)).convert("RGB")
    if h:  # center-crop to aspect then resize
        tr=w/h; ir=im.width/im.height
        if ir>tr:
            nw=int(im.height*tr); x=(im.width-nw)//2; im=im.crop((x,0,x+nw,im.height))
        else:
            nh=int(im.width/tr); y=(im.height-nh)//2; im=im.crop((0,y,im.width,y+nh))
        im=im.resize((w,h),Image.LANCZOS)
    else:
        if im.width>w: im=im.resize((w,int(im.height*w/im.width)),Image.LANCZOS)
    for tp in targets:
        fp=os.path.join(DST,tp); os.makedirs(os.path.dirname(fp),exist_ok=True)
        im.save(fp,"JPEG",quality=q,optimize=True)
    return im.size

# ---- task list: (prompt, targets, w, h) ----
tasks=[]
def add(prompt,targets,w,h=None): tasks.append((prompt,targets if isinstance(targets,list) else [targets],w,h))

# core
add("Aerial view of downtown San Diego skyline and harbor with sailboats on the bay, palm-lined waterfront, and residential hillside neighborhoods in the background, blue sky, golden hour warm light",
    "images/hero.jpg",1600,900)
add("San Diego Bay waterfront with the downtown skyline, palm trees, and sailboats, wide establishing shot, bright clear day",
    "images/og-image.jpg",1200,630)
add("Elegant quality San Diego single-family home exterior, Spanish Revival architecture, well-landscaped front yard, clear blue sky",
    "images/content/why-choose.jpg",1200,800)

# page headers
add("Clean desk with real estate appraisal documents, calculator, pen and a house model, soft office lighting","images/pages/appraisal-fees.jpg",1600,760)
add("Welcoming home office desk with a telephone, laptop and notepad near a window, warm inviting light","images/pages/contact.jpg",1600,760)
add("Tidy desk with an open notebook and a small house figurine, calm neutral tones, question-and-answer theme","images/pages/faq.jpg",1600,760)
add("Charming San Diego residential street with tidy craftsman homes and palm trees, community feeling, sunny","images/pages/reviews.jpg",1600,760)
add("Scenic aerial of San Diego from downtown and the bay out to inland hills, showing varied neighborhoods from coast to valley, bright day","images/pages/service-area.jpg",1600,760)

# services heroes (topical but tasteful)
svc_prompts={
 "date-of-death-appraisals":"Serene classic San Diego single-family home exterior in soft early morning light, established landscaping, quiet and dignified mood",
 "divorce-appraisals":"Two-story suburban San Diego family home exterior, neutral daylight",
 "estate-trust-appraisals":"Elegant older estate-style San Diego home with mature trees and manicured grounds",
 "bankruptcy-appraisals":"Modest well-kept suburban San Diego single-family home, clear day",
 "expert-witness":"Dignified courthouse-style building exterior with columns, California, clear sky, professional",
 "pre-purchase-appraisals":"Attractive San Diego home for sale with a tidy front yard, house keys close-up on foreground table",
 "pre-sale-appraisals":"Staged San Diego home exterior with clean landscaping, bright and inviting",
 "tax-appraisals":"Desk with property tax paperwork, calculator and a small house model, office setting",
 "family-transaction-appraisals":"Warm inviting suburban San Diego family home exterior at golden hour",
 "insurance-dispute-appraisals":"San Diego home exterior under a clear blue sky, well maintained",
 "bail-bond-appraisals":"Solid San Diego single-family home exterior, daytime, secure and established look",
 "immigration-appraisals":"Pleasant San Diego home exterior with an American-suburban feel, bright daylight",
}
for slug,pr in svc_prompts.items():
    add(pr,f"images/services/{slug}.jpg",1600,760)

# service content pool (5) reused across 12 -content files
content_pool=[
 "Professional reviewing real estate appraisal documents and comparable sales printouts at a desk, hands only, no face",
 "Real estate paperwork, a calculator, house keys and a pen arranged on a wooden table, close-up",
 "Front exterior of a quality San Diego single-family home with green lawn, clear day",
 "Hand signing real estate documents on a clipboard, close-up, office lighting",
 "Bright modern living room interior of a San Diego home, tasteful furnishing",
]
content_targets=[f"images/services/{slug}-content.jpg" for slug in svc_prompts]
for i,pr in enumerate(content_pool):
    tgts=content_targets[i::len(content_pool)]
    add(pr,tgts,1000)

# area pools by bucket, reused across the 50 area pages on this site
# (alpine, fallbrook, bonsall, valley-center, pauma-valley, rainbow excluded per site scope)
buckets={
"coastal":["carlsbad","oceanside","encinitas","cardiff-by-the-sea","solana-beach","del-mar","la-jolla","pacific-beach","point-loma","ocean-beach","coronado","imperial-beach"],
"rural":["jamul","ramona","julian","pine-valley","borrego-springs","lakeside"],
"suburban":["rancho-santa-fe","fairbanks-ranch","san-marcos","vista","escondido","poway","carmel-valley","del-sur","4s-ranch","santaluz","rancho-bernardo","rancho-penasquitos","scripps-ranch","sabre-springs","mira-mesa","chula-vista","bonita"],
"urban":["san-diego","mission-hills","north-park","kensington","university-city","clairemont","tierrasanta","del-cerro","national-city","la-mesa","el-cajon","santee","lemon-grove","spring-valley","rancho-san-diego"],
}
bucket_prompts={
"coastal":["Pacific coastal homes on a bluff in San Diego County with ocean view, palm trees, sunny",
           "Beachside residential neighborhood in coastal San Diego County, clear blue water, bright day",
           "Coastal California street with tidy homes and ocean in the distance, golden light",
           "Seaside San Diego County community with lagoon and homes, aerial, clear sky"],
"rural":["Rural San Diego County backcountry property with rolling hills, acreage and oak trees, warm light",
         "Country home on large acreage in the San Diego County backcountry, big sky",
         "San Diego County rural residential land with hills and open space, sunny",
         "Backcountry San Diego County valley with a ranch house and mountains behind, clear day"],
"suburban":["Master-planned suburban San Diego County neighborhood with new homes and tidy streets, aerial, sunny",
            "Well-kept two-story suburban homes in San Diego County, blue sky",
            "San Diego County residential community with parks and family homes, bright daylight",
            "Suburban San Diego County cul-de-sac with attractive homes and green landscaping"],
"urban":["Classic urban San Diego neighborhood with Spanish and craftsman homes on a hillside street, sunny",
         "Established San Diego residential street with mature trees and diverse homes, daytime",
         "Hillside San Diego neighborhood with a distant city and canyon view, clear day",
         "Charming older San Diego bungalow homes on a walkable street, bright light"],
}
for bkt, slugs in buckets.items():
    for pi,pr in enumerate(bucket_prompts[bkt]):
        tgts=[f"images/areas/{slugs[j]}.jpg" for j in range(pi,len(slugs),len(bucket_prompts[bkt]))]
        add(pr,tgts,1600,760)

BUDGET=float(sys.argv[1]) if len(sys.argv)>1 else 36.0
t0=time.time()
log(f"=== RUN {time.strftime('%H:%M:%S')} budget={BUDGET}s total tasks={len(tasks)} ===")
done=0; remaining=0
for i,(pr,tgts,w,h) in enumerate(tasks):
    if all(os.path.exists(os.path.join(DST,t)) for t in tgts):
        continue  # already generated (resume)
    if time.time()-t0>BUDGET:
        remaining+=1; continue
    raw=gen(pr)
    if raw is None:
        log(f"[{i+1}/{len(tasks)}] FAILED -> {tgts[0]}"); continue
    sz=save(raw,tgts,w,h)
    done+=1
    log(f"[{i+1}/{len(tasks)}] ok {sz} -> {len(tgts)} file(s) e.g. {tgts[0]}")
# recount remaining missing
missing=sum(1 for (pr,tgts,w,h) in tasks if not all(os.path.exists(os.path.join(DST,t)) for t in tgts))
log(f"=== PAUSE {time.strftime('%H:%M:%S')} thisrun={done} missing_tasks={missing} ===")
if missing==0:
    open(os.path.join(HERE,"gen_DONE"),"w").write("all")
