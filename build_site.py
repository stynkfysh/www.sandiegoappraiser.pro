#!/usr/bin/env python3
# Static-site generator for www.sandiegoappraiser.pro (Brian Ward Appraisal — San Diego, led by Date of Death Appraisals)
import json, os, html
# ================= Built from the market-area-site TEMPLATE =================
# Localized for the City of San Diego + all of San Diego County (minus the most
# rural North County/backcountry hamlets already covered on sister sites), led
# by Date of Death / estate appraisals. Original copy throughout — not reused
# verbatim from carlsbadappraiser.pro or chula-vista.pro.
# ===============================================================================

OUT  = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(OUT, "areas_all.json")

DOMAIN = "www.sandiegoappraiser.pro"
BASE   = "https://www.sandiegoappraiser.pro"
PHONE_D= "(619) 630-9273"                 # display phone (San Diego County line, same as brianward.com)
PHONE_T= "+16196309273"                   # tel: phone
EMAIL  = "contact@brianward.com"
BRAND  = "Brian Ward Appraisal"
SUBTITLE = "San Diego &amp; San Diego County"
YEAR   = "2026"

def esc(t): return html.escape(str(t), quote=False)

# ---------------- AREA GROUPS (drive service-area + ordering) ----------------
# San Diego city and its neighborhoods lead; full county follows. Dropped vs. the
# countywide master list: alpine, fallbrook, bonsall, valley-center, pauma-valley,
# rainbow (primarily rural areas already the focus of sister North County sites).
GROUPS = [
 ("City of San Diego — Central & Uptown", ["san-diego","mission-hills","north-park","kensington","university-city","clairemont","tierrasanta","del-cerro"]),
 ("City of San Diego — Coastal", ["la-jolla","pacific-beach","point-loma","ocean-beach","coronado"]),
 ("City of San Diego — North City", ["carmel-valley","del-sur","4s-ranch","santaluz","rancho-bernardo","rancho-penasquitos","scripps-ranch","sabre-springs","mira-mesa"]),
 ("North County Coastal", ["carlsbad","oceanside","encinitas","cardiff-by-the-sea","solana-beach","del-mar"]),
 ("North County Inland",  ["san-marcos","vista","escondido","poway"]),
 ("North County Estates", ["rancho-santa-fe","fairbanks-ranch"]),
 ("East County", ["la-mesa","el-cajon","santee","lakeside","lemon-grove","spring-valley","rancho-san-diego"]),
 ("South Bay", ["chula-vista","bonita","national-city","imperial-beach"]),
 ("Backcountry", ["ramona","julian","pine-valley","borrego-springs","jamul"]),
]
ORDER = [s for _,slugs in GROUPS for s in slugs]
POPULAR = ["san-diego","la-jolla","north-park","point-loma","coronado","carlsbad","pacific-beach","mission-hills","encinitas","rancho-bernardo"]
# communities (unincorporated / neighborhoods) get a "(community)" tag on service-area page
INCORPORATED = {"carlsbad","oceanside","encinitas","solana-beach","del-mar","san-marcos","vista","escondido","poway",
 "san-diego","coronado","la-mesa","el-cajon","santee","lemon-grove","chula-vista","national-city","imperial-beach"}

areas = {a["slug"]: a for a in json.load(open(DATA))}
AREA_NAME = {s: areas[s]["name"] for s in ORDER}

# ---------------- SERVICES ----------------
# each: slug, name, card(home blurb), title, desc(meta), h1, lead, sections[(h2,[p...])], llms
# Date of Death Appraisals leads the list — the flagship specialty of this site.
SERVICES = [
{"slug":"date-of-death-appraisals","name":"Date of Death Appraisals",
 "card":"My core specialty: pinpointing a home's fair market value as of a specific past date so an estate can be settled, reported to the IRS, and its stepped-up basis documented correctly.",
 "title":"Date of Death Appraisals in San Diego &amp; San Diego County",
 "desc":"San Diego's date-of-death appraisal specialist. Retrospective valuations for estate settlement, IRS Form 706, and stepped-up basis across the City of San Diego and every San Diego County community. 20+ years, 7,000+ appraisals.",
 "h1":"Date of Death Appraisals — San Diego's Retrospective Valuation Specialist",
 "lead":"When someone passes away owning real property, the IRS and the probate court need to know exactly what that property was worth on the date they died — not today, not last year, but that specific date. This is the assignment I built my practice around: reconstructing San Diego's real estate market as it existed on a past date and delivering a report that satisfies the IRS, the probate court, and every heir at the table.",
 "sections":[
   ("Why Families and Fiduciaries Come to Me for This",["Executors, successor trustees, CPAs, and probate attorneys across San Diego County request a date-of-death appraisal to settle an estate, complete IRS Form 706, divide real property fairly among heirs, or lock in the stepped-up cost basis on an inherited home. A property held in a revocable living trust needs this same date-specific value the moment it becomes irrevocable, so trustees can administer it and report accurately to beneficiaries."]),
   ("Reconstructing a Market That No Longer Exists",["A retrospective appraisal is a different discipline than a same-day valuation. I go back to the comparable sales that actually closed around the date in question — not current listings, not today's prices — and rebuild the market conditions as they stood on that day. The finished report walks through the subject property, the historical comparable evidence, the market context, and a fully supported value conclusion dated precisely to the date of death."]),
   ("USPAP-Compliant and Built for Scrutiny",["Every date-of-death report I write follows USPAP and is organized the way the IRS, San Diego County probate courts, and estate counsel expect to see it. With more than 20 years appraising throughout San Diego and thousands of completed assignments, my conclusions are relied on by attorneys, CPAs, and fiduciaries who need a value that will hold up if it's ever questioned."]),
   ("What Stepped-Up Basis Actually Means for Heirs",["Inherited real estate generally receives a “step-up” in cost basis to its fair market value on the date of death. A properly documented appraisal is what establishes that number — and it's what lets heirs pay capital-gains tax only on appreciation that happens after they inherit, rather than on decades of appreciation the original owner experienced. Skipping this step, or relying on an unsupported guess, can cost heirs real money at tax time."]),
 ],
 "llms":"Date-of-death and other retrospective appraisals for estate settlement, IRS Form 706, and stepped-up basis in San Diego and throughout San Diego County. This is the site's lead specialty. USPAP-compliant, IRS- and probate-court-ready."},

{"slug":"divorce-appraisals","name":"Divorce Appraisals",
 "card":"A neutral opinion of value that holds up for both sides — used by San Diego family-law attorneys, mediators, and the court to divide real property fairly.",
 "title":"Divorce Appraisals in San Diego &amp; San Diego County",
 "desc":"Neutral, court-ready divorce appraisals for family-law matters throughout San Diego and San Diego County. Current-value or date-of-separation valuations, with a two-party option.",
 "h1":"Divorce Appraisals in San Diego &amp; San Diego County",
 "lead":"Splitting up marital real estate starts with agreeing on what it's worth. A divorce appraisal gives both spouses, both attorneys, and if necessary the San Diego County Superior Court a single, independent number neither side can credibly dismiss as biased.",
 "sections":[
   ("One Appraiser, No Side to Take",["I don't work for the husband or the wife — I work for an accurate answer. The same methodology and the same standard of documentation apply no matter who signs the engagement, which is exactly why opposing counsel routinely accepts my reports without a second appraisal. When both spouses agree to retain me jointly, a discounted two-party fee applies."]),
   ("Today's Value, the Separation Date, or Both",["California family law sometimes calls for value as of the date of separation, sometimes as of today, and occasionally both. I'll prepare whichever your case requires — including a retrospective valuation reconstructing the market as it stood on the separation date — so the numbers line up with how your attorney is framing the matter."]),
   ("If It Goes to a Hearing",["Should the valuation be contested, I'm available for deposition or trial testimony, and I write reports in language a judge who isn't a real estate professional can actually follow — which tends to shorten, not lengthen, the dispute."]),
   ("Pricing",["Divorce appraisals follow the standard fee schedule by report type, with the two-party discount applied when both spouses share one engagement."]),
 ],
 "llms":"Neutral divorce appraisals for family-law matters in San Diego and San Diego County. Current or date-of-separation retrospective value, expert testimony available, two-party discount."},

{"slug":"estate-trust-appraisals","name":"Estate &amp; Trust Appraisals",
 "card":"Valuations that support probate, trust distribution, and tax reporting — the everyday companion to date-of-death work for executors and trustees.",
 "title":"Estate &amp; Trust Appraisals in San Diego &amp; San Diego County",
 "desc":"Probate, trust distribution, and general estate appraisals throughout San Diego and San Diego County, prepared for probate courts, trustees, CPAs, and beneficiaries.",
 "h1":"Estate &amp; Trust Appraisals in San Diego &amp; San Diego County",
 "lead":"Beyond the date-of-death valuation itself, estate and trust administration often calls for additional appraisal work — a current value for a pending sale, a second opinion for a disputed distribution, or documentation the IRS or a beneficiary's attorney has requested. I handle that full range of estate and trust valuation work across San Diego County.",
 "sections":[
   ("Administering Probate and Trust Property Fairly",["Whether a home is moving through probate or being distributed out of a living trust, an independent appraisal gives the executor or trustee a defensible number and gives beneficiaries confidence the division is equitable. I work regularly alongside San Diego County probate attorneys, trust administrators, and CPAs."]),
   ("Current Value, Retrospective Value, or Both",["Estate matters frequently require more than one date of value — the date of death, a later distribution date, or the date a co-trustee wants documented. I prepare current and retrospective valuations side by side when a matter calls for it."]),
   ("Reports Written to Survive a Beneficiary Dispute",["Every estate report is USPAP-compliant and organized so an attorney, a CPA, the court, and a skeptical beneficiary can each follow the same logic to the same conclusion — which is usually what keeps an estate moving instead of stalling in a dispute."]),
 ],
 "llms":"Estate, probate, and trust-distribution appraisals in San Diego and San Diego County — current and retrospective values for courts, trustees, CPAs, attorneys, and beneficiaries."},

{"slug":"bankruptcy-appraisals","name":"Bankruptcy Appraisals",
 "card":"An independent value the trustee, the debtor's attorney, and the bankruptcy court can rely on to determine real property equity.",
 "title":"Bankruptcy Appraisals in San Diego &amp; San Diego County",
 "desc":"Independent bankruptcy appraisals accepted by trustees and the bankruptcy court, serving San Diego and every San Diego County community. Fast, USPAP-compliant reports.",
 "h1":"Bankruptcy Appraisals in San Diego &amp; San Diego County",
 "lead":"Chapter 7 and Chapter 13 filings both hinge on an accurate read of the equity in any real property the debtor owns. A credible, independent appraisal is what the trustee needs to evaluate exemptions and what the court relies on to rule on secured claims.",
 "sections":[
   ("Why the Equity Number Matters So Much",["The trustee and the court use the appraised value, net of liens and applicable exemptions, to determine how a property is treated in the filing. An accurate, well-supported number protects a debtor from an inflated equity figure and gives the trustee the documentation needed to sign off without delay."]),
   ("Prepared to the Standard Bankruptcy Courts Expect",["Reports follow USPAP and are formatted the way bankruptcy filings require. I regularly work with both debtor-side and creditor-side attorneys throughout San Diego County."]),
   ("Turnaround Built Around Your Deadline",["Bankruptcy schedules move fast. I'll confirm a realistic timeline up front so the appraisal doesn't become the reason a filing slips."]),
 ],
 "llms":"Independent bankruptcy appraisals accepted by trustees and the bankruptcy court in San Diego and San Diego County. USPAP-compliant, fast turnaround."},

{"slug":"expert-witness","name":"Expert Witness &amp; Litigation Support",
 "card":"A report built to be challenged, and testimony to back it up, when a property's value is contested in court, arbitration, or a tax appeal.",
 "title":"Expert Witness &amp; Litigation Support — San Diego County",
 "desc":"Expert-witness appraisal testimony and litigation support for contested property valuations, tax appeals, and disputes throughout San Diego and San Diego County.",
 "h1":"Expert Witness &amp; Litigation Support — San Diego County",
 "lead":"A litigation appraisal has to do more than reach a defensible number — it has to survive cross-examination. I provide expert-witness testimony and litigation support for real property valuation disputes across San Diego County, including many that originate from contested date-of-death and estate valuations.",
 "sections":[
   ("Written to Anticipate the Challenge",["I document every adjustment and every comparable so the reasoning is transparent from the first page to the conclusion, and I prepare exhibits a judge, jury, or arbitrator without a real estate background can follow without translation."]),
   ("Testimony, Review, and Consulting",["Engagements include deposition and trial testimony, technical review of an opposing appraiser's report, and consulting support for attorneys handling property, partnership, estate, and tax-appeal disputes."]),
   ("Engagement Terms",["Litigation and testimony work is scoped and quoted individually. Contact me early — before a report is finalized, if possible — to discuss the matter, the deadlines, and fee arrangement."]),
 ],
 "llms":"Expert-witness appraisal testimony and litigation support for contested property valuations, tax appeals, and estate disputes in San Diego and San Diego County."},

{"slug":"pre-purchase-appraisals","name":"Pre-Purchase Appraisals",
 "card":"An independent number before you sign — so you know what a San Diego home is actually worth before you commit to buying it.",
 "title":"Pre-Purchase Appraisals in San Diego &amp; San Diego County",
 "desc":"Independent pre-purchase appraisals throughout San Diego and San Diego County. Know a property's real market value before you buy in a competitive market.",
 "h1":"Pre-Purchase Appraisals in San Diego &amp; San Diego County",
 "lead":"San Diego's housing market rewards buyers who know what they're actually looking at. A pre-purchase appraisal gives you an independent, professional opinion of value before you're locked into a contract — separate from whatever number a lender's appraiser eventually produces.",
 "sections":[
   ("A Real Analysis, Not an Algorithm",["An automated home-value estimate can miss the specifics that actually move price — condition, lot, view, recent comparable sales — by a wide margin. A certified appraisal is grounded in a direct analysis of the property itself. It's especially valuable on unique homes, non-contingent offers, and off-market or family purchases where no lender appraisal will ever happen."]),
   ("Leverage at the Negotiating Table",["An independent, documented value gives you something to point to — whether that's supporting a lower offer or confirming the asking price is fair before you waive contingencies."]),
   ("Pricing",["Pre-purchase appraisals follow the standard fee schedule by report type; most single-family homes fall into the published tiers."]),
 ],
 "llms":"Independent pre-purchase appraisals in San Diego and San Diego County. Know a property's true value before you buy and avoid overpaying in a competitive market."},

{"slug":"pre-sale-appraisals","name":"Pre-Sale Appraisals",
 "card":"Price it right the first time — an independent, certified valuation to set your San Diego listing price instead of guessing.",
 "title":"Pre-Sale Appraisals in San Diego &amp; San Diego County",
 "desc":"Pre-sale and pre-listing appraisals throughout San Diego and San Diego County. Set a defensible, realistic asking price backed by an independent valuation.",
 "h1":"Pre-Sale Appraisals in San Diego &amp; San Diego County",
 "lead":"Listing too high wastes market time; listing too low leaves money on the table. A pre-sale appraisal gives you a defensible, independently supported number to build your pricing and marketing strategy around before the sign goes in the yard.",
 "sections":[
   ("Get the Number Right Before You List",["I analyze recent closed comparables and current conditions in your specific San Diego neighborhood to develop a supportable market value. Sellers use the report to set the list price with confidence, and to reassure a buyer's lender later that the price reflects real market data."]),
   ("For FSBO Sellers and Listed Homes Alike",["Whether you're selling without an agent or listing traditionally, an independent appraisal takes the emotion and guesswork out of the pricing decision from day one."]),
   ("Pricing",["Pre-sale appraisals follow the standard fee schedule by report type."]),
 ],
 "llms":"Pre-sale and pre-listing appraisals in San Diego and San Diego County. Set a realistic, defensible asking price with an independent certified valuation."},

{"slug":"tax-appraisals","name":"Tax Appraisals",
 "card":"Support for property-tax appeals, gift-tax reporting, and other tax matters that require a documented, defensible value.",
 "title":"Tax Appraisals in San Diego &amp; San Diego County",
 "desc":"Property-tax appeal and gift-tax appraisals throughout San Diego and San Diego County — documented valuations for the county assessor and the IRS.",
 "h1":"Tax Appraisals in San Diego &amp; San Diego County",
 "lead":"Tax matters involving real property — from a property-tax assessment that looks too high to a gifted property that needs a documented value — require the same rigor as an estate appraisal, just aimed at a different audience: the assessor's office or the IRS.",
 "sections":[
   ("Challenging an Over-Assessment",["If your San Diego County assessed value looks out of step with the market, a well-supported appraisal is the evidence an assessment appeals board expects to see. I prepare the valuation for the correct lien date and organize the comparable evidence to make the case clearly."]),
   ("Gift and Transfer Tax Documentation",["Gifted real estate and certain family transfers must be reported to the IRS at fair market value. A defensible, independent appraisal is what documents that figure and reduces the odds of a later IRS challenge."]),
   ("Pricing",["Tax appraisals are quoted by report type and complexity; a retrospective lien-date assignment may carry an added research fee."]),
 ],
 "llms":"Property-tax appeal and gift-tax appraisals in San Diego and San Diego County for the county assessor and the IRS."},

{"slug":"family-transaction-appraisals","name":"Family Transaction Appraisals",
 "card":"A documented fair-market value for sales, gifts, and transfers between family members — the kind of paper trail the IRS expects to see.",
 "title":"Family Transaction Appraisals in San Diego &amp; San Diego County",
 "desc":"IRS-ready family-transaction appraisals for sales, gifts, and transfers between relatives throughout San Diego and San Diego County.",
 "h1":"Family Transaction Appraisals in San Diego &amp; San Diego County",
 "lead":"A sale from parent to child, a gift of real property, or any transfer between relatives is expected by the IRS to reflect fair market value — even when no outside buyer is ever involved. An independent appraisal is what documents that value and protects everyone named in the transaction.",
 "sections":[
   ("Documenting a Genuinely Fair Price",["Whether it's a parent selling to a child at a friendly price or co-owners untangling a shared property, the transaction should be anchored to a real market-based value. My report supplies that figure along with the comparable evidence behind it."]),
   ("Reducing IRS and Family Friction",["A credible, USPAP-compliant appraisal lowers the odds of an IRS challenge later and gives every family member a shared, neutral reference point instead of a number one side picked."]),
   ("Pricing",["Family-transaction appraisals follow the standard fee schedule by report type."]),
 ],
 "llms":"IRS-ready family-transaction appraisals for sales, gifts, and transfers between family members in San Diego and San Diego County."},

{"slug":"insurance-dispute-appraisals","name":"Insurance Dispute Appraisals",
 "card":"Objective evidence when you and your insurance carrier disagree about what a property, or a loss, is actually worth.",
 "title":"Insurance Dispute Appraisals in San Diego &amp; San Diego County",
 "desc":"Insurance claim and coverage-dispute appraisals throughout San Diego and San Diego County — independent valuations addressing market value, replacement questions, and policy limits.",
 "h1":"Insurance Dispute Appraisals in San Diego &amp; San Diego County",
 "lead":"When a carrier's number and your own sense of a property's value don't match, an independent appraisal supplies the objective evidence that actually moves a stalled claim toward resolution.",
 "sections":[
   ("Documented Support for Your Position",["An impartial, well-supported appraisal gives you something concrete to bring back to the adjuster when a carrier's initial figure looks low."]),
   ("Written for Adjusters, Attorneys, and if Needed the Court",["Reports follow USPAP and are written clearly enough for an adjuster or attorney to act on without a real estate background — and structured to hold up if the dispute ends up in front of a judge."]),
   ("Pricing",["Insurance-dispute assignments are quoted individually based on scope and complexity."]),
 ],
 "llms":"Insurance claim and coverage-dispute appraisals in San Diego and San Diego County. Independent valuations addressing market value, replacement questions, and policy limits."},

{"slug":"bail-bond-appraisals","name":"Bail Bond Appraisals",
 "card":"A fast, credible valuation to verify the equity in real property pledged as bail collateral.",
 "title":"Bail Bond Appraisals in San Diego &amp; San Diego County",
 "desc":"Bail-bond property appraisals throughout San Diego and San Diego County — reports accepted by courts and bonding companies to verify real property equity.",
 "h1":"Bail Bond Appraisals in San Diego &amp; San Diego County",
 "lead":"When real property secures a bail bond, both the court and the bonding company need a credible, independent number verifying the equity behind it — usually on a tight clock.",
 "sections":[
   ("Verifying What's Actually Pledged",["The bond amount is tied directly to the equity available in the pledged property. A documented market value combined with a clear accounting of existing liens establishes exactly how much collateral is really there."]),
   ("Built for a Tight Timeline",["These assignments almost always come with a short deadline. I move quickly and format the finished report so the court and the bonding company can act on it without follow-up questions."]),
   ("Pricing",["Bail-bond appraisals follow the standard fee schedule by report type; rush turnaround can be arranged."]),
 ],
 "llms":"Bail-bond property appraisals in San Diego and San Diego County, accepted by courts and bonding companies to verify real property equity for collateral."},

{"slug":"immigration-appraisals","name":"Immigration Appraisals",
 "card":"Independent property valuations documenting real-estate assets for USCIS visa, residency, and sponsorship filings.",
 "title":"Immigration Appraisals in San Diego &amp; San Diego County",
 "desc":"Immigration appraisals for USCIS petitions, visa applications, and residency filings throughout San Diego and San Diego County — reports built to federal documentation standards.",
 "h1":"Immigration Appraisals in San Diego &amp; San Diego County",
 "lead":"Certain immigration filings require documented proof of a sponsor's or applicant's real-estate holdings. I provide independent appraisals that meet USCIS documentation expectations for visa, residency, and sponsorship petitions.",
 "sections":[
   ("Documenting the Real-Estate Side of a Filing",["Whether the petition needs to establish a sponsor's net worth or an applicant's own asset holdings, a certified appraisal supplies a current, well-supported value with the evidence behind it."]),
   ("Prepared for Federal-Level Review",["Reports are USPAP-compliant and organized to meet the documentation standards immigration filings are held to."]),
   ("Pricing",["Immigration appraisals follow the standard fee schedule by report type."]),
 ],
 "llms":"Immigration appraisals for USCIS petitions, visa applications, and residency filings in San Diego and San Diego County."},
]
SVC = {s["slug"]: s for s in SERVICES}
FOOT_SVC = ["date-of-death-appraisals","divorce-appraisals","estate-trust-appraisals","bankruptcy-appraisals",
            "expert-witness","pre-purchase-appraisals","pre-sale-appraisals","tax-appraisals"]

# ---------------- shared building blocks ----------------
def business_ld():
    areaserved = ", ".join(
        '{"@type": "City", "name": "%s"}' % AREA_NAME[s].replace('"',"") for s in ORDER)
    return ('{"@context": "https://schema.org", "@type": ["RealEstateAgent", "ProfessionalService", "LocalBusiness"], '
      '"@id": "%s/#business", "name": "%s", '
      '"description": "California Certified Residential Real Estate Appraiser serving San Diego and all of San Diego County, specializing in date-of-death and estate appraisals, plus divorce, bankruptcy, expert witness, pre-purchase and pre-sale appraisals.", '
      '"url": "%s/", "telephone": "%s", "email": "%s", "image": "%s/images/og-image.jpg", "logo": "%s/images/og-image.jpg", '
      '"priceRange": "$$", "foundingDate": "2004", '
      '"parentOrganization": {"@type": "Organization", "name": "Brian Ward Appraisal", "url": "https://www.brianward.com", "sameAs": "https://www.brianward.com"}, '
      '"brand": {"@type": "Brand", "name": "Brian Ward Appraisal", "url": "https://www.brianward.com"}, '
      '"sameAs": ["https://www.brianward.com"], '
      '"address": {"@type": "PostalAddress", "addressLocality": "San Diego", "addressRegion": "CA", "addressCountry": "US"}, '
      '"geo": {"@type": "GeoCoordinates", "latitude": "32.7157", "longitude": "-117.1611"}, '
      '"areaServed": [%s], '
      '"knowsAbout": ["Real estate appraisal", "Date of death appraisal", "Divorce appraisal", "Estate appraisal", "Retrospective appraisal", "USPAP", "Stepped-up basis", "Expert witness testimony", "Property tax appeal"], '
      '"serviceType": ["Date of Death Appraisals", "Divorce Appraisals", "Estate & Trust Appraisals", "Bankruptcy Appraisals", "Expert Witness & Litigation Support", "Pre-Purchase Appraisals", "Pre-Sale Appraisals", "Tax Appraisals", "Family Transaction Appraisals", "Insurance Dispute Appraisals", "Bail Bond Appraisals", "Immigration Appraisals"], '
      '"openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"}}'
    ) % (BASE, BRAND, BASE, PHONE_D, EMAIL, BASE, BASE, areaserved)

def head(p, title, desc, canon, ogimg, extra_ld=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {BRAND}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="{BRAND}">
<meta name="geo.region" content="US-CA">
<meta name="geo.placename" content="San Diego, San Diego County, California">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} | {BRAND}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{ogimg}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} | {BRAND}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimg}">
<meta name="theme-color" content="#16324a">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{p}styles.css">
<link rel="icon" href="{p}images/favicon.svg" type="image/svg+xml">
<script type="application/ld+json">{business_ld()}</script>
{extra_ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap header-inner"><a href="{p}index.html" class="brand"><span class="brand-mark">BW</span><span class="brand-txt"><strong>{BRAND}</strong><small>{SUBTITLE}</small></span></a>
<button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">&#9776;</button>
<nav class="nav-links">
  <a href="{p}index.html">Home</a>
  <a href="{p}appraisal-fees.html">Services &amp; Fees</a>
  <a href="{p}service-area.html">Service Area</a>
  <a href="{p}faq.html">FAQ</a>
  <a href="{p}reviews.html">Reviews</a>
  <a href="{p}contact.html" class="nav-cta">Get a Quote</a>
</nav></div></header>
<main id="main">
'''

def footer(p):
    svc = "\n".join(f'<li><a href="{p}services/{s}.html">{SVC[s]["name"]}</a></li>' for s in FOOT_SVC)
    pop = "\n".join(f'<li><a href="{p}areas/{s}.html">{AREA_NAME[s]}</a></li>' for s in POPULAR)
    return f'''</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div class="foot-col foot-about">
      <div class="foot-brand">{BRAND}</div>
      <p>California Certified Residential Real Estate Appraiser serving San Diego and all of San Diego County since 2004, specializing in date-of-death and estate appraisals. 20+ years of experience, 7,000+ appraisals completed.</p>
      <p class="foot-contact">
        <a href="tel:{PHONE_T}">{PHONE_D}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </p>
      <p class="foot-parent">sandiegoappraiser.pro is the San Diego date-of-death appraisal site of <a href="https://www.brianward.com">Brian Ward Appraisal</a>. Visit our main site <a href="https://www.brianward.com"><strong>brianward.com</strong></a>, serving San Diego &amp; Riverside Counties.</p>
    </div>
    <div class="foot-col">
      <h3>Appraisal Services</h3>
      <ul>{svc}</ul>
    </div>
    <div class="foot-col">
      <h3>Popular Areas</h3>
      <ul>{pop}</ul>
    </div>
    <div class="foot-col">
      <h3>Company</h3>
      <ul>
        <li><a href="https://www.brianward.com"><strong>Main Site: brianward.com</strong></a></li>
        <li><a href="{p}index.html">Home</a></li>
        <li><a href="{p}appraisal-fees.html">Services &amp; Fees</a></li>
        <li><a href="{p}service-area.html">Service Area</a></li>
        <li><a href="{p}faq.html">FAQ</a></li>
        <li><a href="{p}reviews.html">Reviews</a></li>
        <li><a href="{p}contact.html">Contact</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bar"><div class="wrap">&copy; {YEAR} {BRAND}. All rights reserved. California Certified Residential Real Estate Appraiser. Serving San Diego &amp; San Diego County, CA.</div></div>
</footer>
<script src="{p}main.js" defer></script>
</body>
</html>'''

GRAD = "linear-gradient(120deg,rgba(9,25,38,.88) 0%,rgba(22,50,74,.76) 55%,rgba(216,103,47,.42) 100%)"

def cta_band(p, h2="Ready to get started?", sub=None):
    sub = sub or f'Request an appraisal online or call directly at <a href="tel:{PHONE_T}">{PHONE_D}</a>.'
    return f'''<section class="cta-band"><div class="wrap">
  <h2>{h2}</h2>
  <p>{sub}</p>
  <div class="cta-row">
    <a class="btn btn-light" href="{p}contact.html">Get Your Free Quote &rarr;</a>
    <a class="btn btn-outline-light" href="tel:{PHONE_T}">Call {PHONE_D}</a>
  </div>
</div></section>
'''

def write(relpath, content):
    fp = os.path.join(OUT, relpath)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(content)

def crumb(p, items):  # items: list of (name, href or None)
    parts=[]
    for i,(n,h) in enumerate(items):
        if h: parts.append(f'<a href="{p}{h}">{n}</a>')
        else: parts.append(f'<span aria-current="page">{n}</span>')
    sep=' <span class="sep">&rsaquo;</span> '
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><div class="wrap">{sep.join(parts)}</div></nav>\n'

# ---------------- INDEX ----------------
def build_index():
    p=""
    svc_cards="\n".join(
        f'''<a class="svc-card" href="services/{s['slug']}.html">
  <h3>{s['name']}</h3>
  <p>{esc(s['card'])}</p>
  <span class="svc-more">Learn more &rarr;</span>
</a>''' for s in SERVICES)
    chips="\n".join(f'<a class="chip" href="areas/{s}.html">{AREA_NAME[s]}</a>' for s in ORDER)
    body=f'''{head(p,"San Diego Date of Death &amp; Estate Appraiser","San Diego's date-of-death appraisal specialist. Certified residential real estate appraiser serving the City of San Diego and every San Diego County community. Estate, divorce, and pre-purchase appraisals. 20+ years, 7,000+ appraisals.",f"{BASE}/index.html",f"{BASE}/images/og-image.jpg")}<section class="hero">
  <div class="hero-overlay"></div>
  <div class="wrap hero-inner">
    <div class="hero-eyebrow">California Certified Residential Appraiser &bull; Since 2004</div>
    <h1>San Diego's Date-of-Death &amp; Estate Appraisal Specialist</h1>
    <p class="hero-sub">Independent, retrospective valuations for estates, trusts, and probate throughout San Diego and San Diego County &mdash; plus divorce, bankruptcy, and pre-purchase appraisals &mdash; written to withstand scrutiny from the IRS, attorneys, and the court.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="contact.html">Get Your Free Quote &rarr;</a>
      <a class="btn btn-outline" href="tel:{PHONE_T}">Call {PHONE_D}</a>
    </div>
    <div class="hero-stats">
      <div><strong>20+</strong><span>Years Experience</span></div>
      <div><strong>7,000+</strong><span>Appraisals Completed</span></div>
      <div><strong>{len(ORDER)}</strong><span>Communities Served</span></div>
    </div>
  </div>
</section>

<section class="section"><div class="wrap">
  <div class="section-head">
    <h2>Appraisal Services</h2>
    <p>Independent, non-lender appraisals for attorneys, courts, estates, families, and individuals throughout San Diego and San Diego County &mdash; led by date-of-death and estate valuation work.</p>
  </div>
  <div class="svc-grid">{svc_cards}</div></div></section>

<section class="section section-alt"><div class="wrap">
  <div class="section-head"><h2>Why Choose Brian Ward Appraisal</h2>
  <p>Decades of local experience and reports built to hold up under scrutiny.</p></div>
  <figure class="content-figure"><img loading="lazy" src="images/content/why-choose.jpg" alt="Quality San Diego County coastal home valued by Brian Ward Appraisal"></figure>
  <div class="why-grid">
    <div class="why-item"><h3>Certified &amp; Experienced</h3><p>California Certified Residential Appraiser with 20+ years of experience and 7,000+ completed appraisals across San Diego County.</p></div>
    <div class="why-item"><h3>Direct Communication</h3><p>Work directly with the appraiser &mdash; no call centers, no runaround. Personal attention from start to finish.</p></div>
    <div class="why-item"><h3>Reports That Withstand Scrutiny</h3><p>Every report is written to be clearly understood by attorneys, judges, the IRS, and financial institutions, with defensible conclusions.</p></div>
    <div class="why-item"><h3>Deep Local Knowledge</h3><p>From downtown high-rises and La Jolla's coastal bluffs to North County, East County, and the South Bay, I know San Diego's neighborhoods and micro-markets block by block.</p></div>
    <div class="why-item"><h3>Responsive Service</h3><p>I work efficiently to meet court deadlines and time-sensitive transactions. Contact me to discuss your timeline.</p></div>
    <div class="why-item"><h3>Fair, Transparent Pricing</h3><p>Published fees starting at $299 with no hidden charges. Complex properties and rush delivery are quoted upfront.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Serving All of San Diego County</h2>
  <p>From downtown San Diego to the North County coast, East County, and the South Bay &mdash; click any community to learn about appraisal services in that area.</p></div>
  <div class="chip-cloud">{chips}</div>
  <p class="center"><a class="btn btn-primary" href="service-area.html">View the Full Service Area &rarr;</a></p>
</div></section>

{cta_band(p)}{footer(p)}'''
    write("index.html", body)

# ---------------- SERVICE PAGES ----------------
def build_service(s):
    p="../"; slug=s["slug"]
    others="\n".join(f'<li><a href="{o["slug"]}.html">{o["name"]}</a></li>' for o in SERVICES if o["slug"]!=slug)
    secs=""
    for h2,paras in s["sections"]:
        secs+=f"<h2>{h2}</h2>\n"+"".join(f"<p>{para}</p>\n" for para in paras)
    canon=f"{BASE}/services/{slug}.html"
    ogimg=f"{BASE}/images/services/{slug}.jpg"
    extra=(f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "Services & Fees", "item": "{BASE}/appraisal-fees.html"}}, {{"@type": "ListItem", "position": 3, "name": "{s["name"].replace("&amp;","&")}", "item": "{canon}"}}]}}</script>\n'
      f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Service", "serviceType": "{s["name"].replace("&amp;","&")}", "name": "{s["name"].replace("&amp;","&")}", "description": "{s["desc"].replace("&amp;","&")}", "provider": {{"@id": "{BASE}/#business"}}, "areaServed": {{"@type": "AdministrativeArea", "name": "San Diego County, California"}}, "url": "{canon}"}}</script>\n')
    body=head(p, s["title"], s["desc"], canon, ogimg, extra)
    body+=crumb(p, [("Home","index.html"),("Services & Fees","appraisal-fees.html"),(s["name"],None)])
    body+=f'''<section class="page-head has-hero" style="background-image:{GRAD},url('../images/services/{slug}.jpg')"><div class="wrap"><h1>{s["h1"]}</h1></div></section>
<section class="section"><div class="wrap content-grid">
  <article class="content-main">
    <p class="lead">{s["lead"]}</p>
    <figure class="content-figure"><img loading="lazy" src="../images/services/{slug}-content.jpg" alt="{s['name'].replace('&amp;','and')} — San Diego County real estate appraisal"></figure>
    {secs}    <h2>Request This Appraisal</h2>
    <p>Published fees start at $299; your exact fee is confirmed before you commit. See the full <a href="../appraisal-fees.html">fee schedule</a> or <a href="../contact.html">request a free quote</a>.</p>
  </article>
  <aside class="content-aside">
    <div class="aside-card">
      <h3>Request This Appraisal</h3>
      <p>Call <a href="tel:{PHONE_T}">{PHONE_D}</a> or request a free quote online.</p>
      <a class="btn btn-primary btn-block" href="../contact.html">Get a Free Quote</a>
    </div>
    <div class="aside-card">
      <h3>Other Services</h3>
      <ul class="aside-links">{others}</ul>
    </div>
  </aside>
</div></section>
{cta_band(p, h2=f"Need a {s['name'].replace('&amp;','and')} appraisal?")}'''
    body+=footer(p)
    write(f"services/{slug}.html", body)

# ---------------- AREA PAGES ----------------
def build_area(slug):
    a=areas[slug]; p="../"
    name=esc(a["name"]); canon=f"{BASE}/areas/{slug}.html"; ogimg=f"{BASE}/images/areas/{slug}.jpg"
    svc_links="\n".join(f'<li><a href="../services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    nb="\n".join(f'<li><a href="{n}.html">{AREA_NAME.get(n,n)}</a></li>' for n in a["nearby"] if n in AREA_NAME)
    hoods="".join(f"<li>{esc(h)}</li>" for h in a["neighborhoods"])
    title=f"Real Estate Appraiser in {name}, CA — Date of Death, Divorce, Estate"
    desc=f"Certified residential real estate appraiser in {name}, California. Date-of-death, divorce, estate, and pre-purchase appraisals in {name} and San Diego County. Call {PHONE_D}."
    extra=(f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "Service Area", "item": "{BASE}/service-area.html"}}, {{"@type": "ListItem", "position": 3, "name": "{name}", "item": "{canon}"}}]}}</script>\n'
      f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Place", "name": "{name}, California", "address": {{"@type": "PostalAddress", "addressLocality": "{name}", "addressRegion": "CA", "addressCountry": "US"}}}}</script>\n'
      f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "RealEstateAgent", "@id": "{BASE}/#business", "name": "{BRAND}", "telephone": "{PHONE_D}", "areaServed": {{"@type": "City", "name": "{name}, California"}}, "url": "{canon}"}}</script>\n')
    body=head(p, title, desc, canon, ogimg, extra)
    body+=crumb(p, [("Home","index.html"),("Service Area","service-area.html"),(a["name"],None)])
    body+=f'''<section class="page-head has-hero area-head" style="background-image:{GRAD},url('../images/areas/{slug}.jpg')"><div class="wrap"><span class="region-tag">{esc(a["region_tag"])}</span><h1>Real Estate Appraiser in {name}, California</h1></div></section>
<section class="section"><div class="wrap content-grid">
  <article class="content-main">
    <p class="lead">{esc(a["lead"])}</p>
    <h2>{name} Real Estate Market</h2>
    <p>{esc(a["market"])}</p>
    <p>Whether you're settling an <a href="../services/estate-trust-appraisals.html">estate</a>, navigating a <a href="../services/divorce-appraisals.html">divorce</a>, establishing a <a href="../services/date-of-death-appraisals.html">date-of-death value</a>, or planning a purchase or sale, a certified independent appraisal gives you a defensible opinion of value for property in {name}.</p>
    <h3>Notable {name} Neighborhoods &amp; Communities</h3>
    <ul class="pill-list">{hoods}</ul>
    <h2>Local Highlights</h2>
    <p>{esc(a["highlights"])}</p>
    <h2>Local Valuation Considerations</h2>
    <p>{esc(a["valuation"])}</p>
    <h2>Appraisal Services Available in {name}</h2>
    <ul class="two-col-links">{svc_links}</ul>
  </article>
  <aside class="content-aside">
    <div class="aside-card">
      <h3>{name} Appraisals</h3>
      <p>ZIP codes: {esc(a["zips"])}</p>
      <p>Call <a href="tel:{PHONE_T}">{PHONE_D}</a> or request a quote online for a certified appraisal in {name}.</p>
      <a class="btn btn-primary btn-block" href="../contact.html">Get a Free Quote</a>
    </div>
    <div class="aside-card">
      <h3>Nearby Areas</h3>
      <ul class="aside-links">{nb}</ul>
    </div>
  </aside>
</div></section>
{cta_band(p, h2=f"Need an appraisal in {name}?")}'''
    body+=footer(p)
    write(f"areas/{slug}.html", body)

# ---------------- FEES ----------------
def build_fees():
    p=""
    rows=[("Basic Desktop","$299","Records-based valuation with no property visit. MLS data, county records, and recent comparable sales analysis."),
          ("Desktop Appraisal","$449","Enhanced records review, neighborhood analysis, and detailed comparable sales study. No property visit."),
          ("Drive-By Appraisal","$575","Exterior-only inspection with photographs. Includes property condition notes and full market analysis."),
          ("Standard (Single Family)","$625","Full interior and exterior inspection with detailed property photographs. Complete narrative appraisal report."),
          ("Desktop (2–4 Unit)","$550","Multi-unit records-based valuation with separate unit analysis. No property visit."),
          ("Standard (2–4 Unit)","$725","Multi-unit full interior and exterior inspection. Separate unit analysis and complete narrative report.")]
    trow="".join(f'<tr><td><strong>{n}</strong></td><td class="price">{pr}</td><td>{d}</td></tr>' for n,pr,d in rows)
    fee_svc="".join(f'<a class="fee-svc" href="services/{s["slug"]}.html"><h3>{s["name"]}</h3><p>{esc(s["card"])}</p></a>' for s in SERVICES)
    canon=f"{BASE}/appraisal-fees.html"
    extra=f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "Services & Fees", "item": "{canon}"}}]}}</script>\n'
    body=head(p,"Appraisal Services &amp; Fees — San Diego &amp; San Diego County","Transparent appraisal pricing starting at $299. Date-of-death, estate, divorce, pre-purchase, and expert-witness appraisals throughout San Diego and San Diego County, CA.",canon,f"{BASE}/images/pages/appraisal-fees.jpg",extra)
    body+=crumb(p,[("Home","index.html"),("Services & Fees",None)])
    body+=f'''<section class="page-head has-hero" style="background-image:{GRAD},url('images/pages/appraisal-fees.jpg')"><div class="wrap"><h1>Appraisal Services &amp; Fees</h1><p>Transparent pricing for date-of-death, estate, divorce, litigation, pre-purchase, and specialized appraisals throughout San Diego and San Diego County.</p></div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Appraisal Pricing</h2><p>Competitive, transparent rates. All prices include a written report suitable for courts, attorneys, and the IRS. Fees listed are starting prices &mdash; complex, high-liability, large-acreage, or rush properties may be higher, and your exact fee is quoted before you commit.</p></div>
  <div class="table-wrap"><table class="price-table"><thead><tr><th>Service Type</th><th>Price</th><th>What's Included</th></tr></thead><tbody>{trow}</tbody></table></div>
  <div class="note-cards">
    <div class="note-card"><h3>What You Receive</h3><p>A professional written report suitable for courts, attorneys, the IRS, lenders, and financial institutions &mdash; delivered digitally, with comprehensive market analysis, property description, and a defensible value conclusion.</p></div>
    <div class="note-card"><h3>Turnaround Time</h3><p>Most residential reports are completed within several business days. I work efficiently to meet court deadlines and time-sensitive transactions &mdash; contact me to discuss your timeline.</p></div>
    <div class="note-card"><h3>Payment Options</h3><p>Payment by credit card, check, or electronic transfer, due upon completion. Contact me to discuss invoice terms for large assignments or multi-property estate work.</p></div>
  </div>
</div></section>
<section class="section section-alt"><div class="wrap">
  <div class="section-head"><h2>Our Appraisal Services</h2><p>Specialized valuations for every situation, from family transactions to court proceedings.</p></div>
  <div class="fee-svc-grid">{fee_svc}</div>
</div></section>
{cta_band(p, h2="Ready to request an appraisal?")}'''
    body+=footer(p)
    write("appraisal-fees.html", body)

# ---------------- SERVICE AREA ----------------
def build_service_area():
    p=""
    blocks=""
    for gname,slugs in GROUPS:
        lis=""
        for s in slugs:
            tag="" if s in INCORPORATED else ' <em>(community)</em>'
            lis+=f'<li><a href="areas/{s}.html">{AREA_NAME[s]}{tag}</a></li>\n'
        blocks+=f'''<div class="region-block">
  <h3>{gname} <span class="region-count">{len(slugs)} areas</span></h3>
  <ul class="area-list">{lis}</ul>
</div>'''
    canon=f"{BASE}/service-area.html"
    extra=f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "Service Area", "item": "{canon}"}}]}}</script>\n'
    body=head(p,"Service Area — San Diego &amp; San Diego County Appraiser","Certified residential appraisals throughout the City of San Diego and San Diego County, CA: La Jolla, North Park, Point Loma, Carlsbad, Chula Vista, Escondido, and 45+ more cities and communities.",canon,f"{BASE}/images/pages/service-area.jpg",extra)
    body+=crumb(p,[("Home","index.html"),("Service Area",None)])
    body+=f'''<section class="page-head has-hero" style="background-image:{GRAD},url('images/pages/service-area.jpg')"><div class="wrap"><h1>San Diego County Appraisal Service Area</h1><p>Brian Ward Appraisal is centered on the City of San Diego and provides certified residential appraisals across all of San Diego County, California &mdash; from downtown and the coast to North County, East County, the South Bay, and the accessible backcountry. Select your city or community below.</p></div></section>
<section class="section"><div class="wrap">
  <div class="region-grid">{blocks}</div>
</div></section>
{cta_band(p)}'''
    body+=footer(p)
    write("service-area.html", body)

# ---------------- FAQ ----------------
def build_faq():
    p=""
    qas=[
     ("Do you specialize in date-of-death appraisals?","Yes — date-of-death and other retrospective estate valuations are the core of my practice. I regularly work with San Diego County executors, successor trustees, CPAs, and probate attorneys to establish IRS- and court-ready fair market value as of a specific past date for estate settlement and stepped-up basis."),
     ("What areas do you serve?","I provide certified residential appraisal services centered on the City of San Diego and its neighborhoods — Downtown, La Jolla, North Park, Point Loma, Rancho Bernardo, and more — and extending throughout San Diego County, including Carlsbad, Oceanside, Encinitas, San Marcos, Escondido, Poway, Rancho Santa Fe, Coronado, Chula Vista, the South Bay, East County, and Ramona and Julian in the backcountry."),
     ("How much does an appraisal cost?","Residential appraisals start at $299 for a Basic Desktop report and range up to $725 for a full Standard appraisal of a 2–4 unit property. See the Services &amp; Fees page for the full price list. Complex, high-value, large-acreage, or rush assignments may be quoted individually, and your exact fee is always confirmed before you commit."),
     ("Are you a licensed and certified appraiser?","Yes. Brian Ward is a California Certified Residential Real Estate Appraiser with more than 20 years of experience and over 7,000 appraisals completed. All reports comply with USPAP, the Uniform Standards of Professional Appraisal Practice."),
     ("What is the difference between an appraisal and a Zestimate or online estimate?","Online estimates are automated guesses based on limited public data and can be off by tens of thousands of dollars. A certified appraisal is an independent professional opinion of value, supported by a careful analysis of comparable sales and the specific characteristics of your property, and it carries the credibility required by the IRS, courts, and attorneys."),
     ("How long does an appraisal take?","Turnaround depends on the property and the type of report, but most residential appraisals are completed within several business days. I work efficiently to meet probate and court deadlines and time-sensitive transactions — contact me to discuss your timeline."),
     ("What exactly is a retrospective appraisal?","A retrospective appraisal values a property as of a specific past date rather than today — most commonly the date of a person's death for estate and stepped-up basis purposes, or a date of separation in a divorce. I analyze the comparable sales and market conditions that actually existed on that historical date, not current listings."),
     ("Do you appraise coastal, view, urban, and rural properties?","Yes. San Diego and San Diego County range from downtown high-rise condos and La Jolla oceanfront homes to view estates in Rancho Santa Fe and larger acreage parcels in Ramona and Julian. I have deep experience valuing everything from dense urban condos to non-standard rural and equestrian properties."),
     ("How is this site related to brianward.com?","sandiegoappraiser.pro is the City of San Diego and San Diego County-focused site of Brian Ward Appraisal, led by date-of-death and estate valuation work. The main company site, brianward.com, serves both San Diego and Riverside Counties across all appraisal purposes. It is the same appraiser and the same USPAP-compliant reports."),
     ("How do I order an appraisal?",f"Call {PHONE_D}, email {EMAIL}, or complete the online form on the Contact page. I'll review your needs, confirm the fee, and schedule the assignment."),
    ]
    ld_q=", ".join('{"@type": "Question", "name": "%s", "acceptedAnswer": {"@type": "Answer", "text": "%s"}}'%(q.replace('&amp;','&').replace('"',"'"), a.replace('&amp;','&').replace('"',"'")) for q,a in qas)
    faq_ld='{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [%s]}'%ld_q
    items="\n".join(f'<details class="faq-item"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q,a in qas)
    canon=f"{BASE}/faq.html"
    extra=(f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "FAQ", "item": "{canon}"}}]}}</script>\n'
      f'<script type="application/ld+json">{faq_ld}</script>\n')
    body=head(p,"FAQ — San Diego Date of Death &amp; Appraisal Questions","Answers about date-of-death and retrospective appraisals, appraisal cost, turnaround, certification, and ordering throughout San Diego and San Diego County.",canon,f"{BASE}/images/pages/faq.jpg",extra)
    body+=crumb(p,[("Home","index.html"),("FAQ",None)])
    body+=f'''<section class="page-head has-hero" style="background-image:{GRAD},url('images/pages/faq.jpg')"><div class="wrap"><h1>Frequently Asked Questions</h1><p>Answers to common questions about date-of-death, estate, and other residential appraisals in San Diego and San Diego County.</p></div></section>
<section class="section"><div class="wrap narrow">
  <div class="faq-list">{items}</div>
</div></section>
{cta_band(p)}'''
    body+=footer(p)
    write("faq.html", body)

# ---------------- REVIEWS (honest, no fabricated testimonials) ----------------
def build_reviews():
    p=""
    canon=f"{BASE}/reviews.html"
    extra=f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "Reviews", "item": "{canon}"}}]}}</script>\n'
    body=head(p,"Reviews &amp; Client References — San Diego &amp; San Diego County","Why San Diego probate attorneys, executors, and homeowners choose Brian Ward Appraisal for date-of-death and estate valuation work. Leave a review or read about our approach.",canon,f"{BASE}/images/pages/reviews.jpg",extra)
    body+=crumb(p,[("Home","index.html"),("Reviews",None)])
    body+=f'''<section class="page-head has-hero" style="background-image:{GRAD},url('images/pages/reviews.jpg')"><div class="wrap"><h1>Reviews &amp; Client References</h1><p>Trusted by probate attorneys, CPAs, executors, and homeowners across San Diego and San Diego County.</p></div></section>
<section class="section"><div class="wrap narrow">
  <p class="lead">More than two decades and 7,000+ completed appraisals later, the reputation this practice runs on comes down to how each report gets written: carefully, independently, and to a standard that holds up when someone pushes back on it.</p>
  <p>The clients who come back most often &mdash; probate and estate attorneys, CPAs, trustees, and San Diego homeowners &mdash; tend to say the same few things: the report showed up on schedule, the analysis was easy to follow, and the value conclusion held up when it mattered, whether that was an IRS review or a beneficiary's second opinion. Rather than post anonymous quotes here, I'd rather earn your own firsthand review.</p>
  <h2>Leave a Review</h2>
  <p>If I've completed an appraisal for you, I'd genuinely appreciate your feedback. You can leave a review on the Brian Ward Appraisal Google Business profile, or email your comments directly to <a href="mailto:{EMAIL}">{EMAIL}</a>. It helps other San Diego families, fiduciaries, and attorneys find a valuation they can trust.</p>
  <h2>What Clients Can Expect</h2>
  <ul class="pill-list"><li>Direct work with the appraiser</li><li>Clear, defensible reports</li><li>On-time delivery</li><li>USPAP compliance</li><li>Fair, transparent fees</li><li>Testimony when needed</li></ul>
  <p class="disclaimer">Brian Ward Appraisal provides independent, non-lender residential appraisals throughout San Diego and San Diego County. References for attorneys and fiduciaries are available on request for qualifying assignments.</p>
</div></section>
{cta_band(p)}'''
    body+=footer(p)
    write("reviews.html", body)

# ---------------- CONTACT ----------------
def build_contact():
    p=""
    canon=f"{BASE}/contact.html"
    serving=", ".join(AREA_NAME[s] for s in ["san-diego","la-jolla","point-loma","north-park","carlsbad","encinitas","san-marcos","escondido","poway","rancho-santa-fe","coronado","chula-vista"])
    extra=f'<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/index.html"}}, {{"@type": "ListItem", "position": 2, "name": "Contact", "item": "{canon}"}}]}}</script>\n'
    body=head(p,"Contact / Order an Appraisal — San Diego &amp; San Diego County",f"Contact Brian Ward Appraisal for a San Diego date-of-death, estate, or other residential appraisal. Call {PHONE_D}, email {EMAIL}, or order online.",canon,f"{BASE}/images/pages/contact.jpg",extra)
    body+=crumb(p,[("Home","index.html"),("Contact",None)])
    body+=f'''<section class="page-head has-hero" style="background-image:{GRAD},url('images/pages/contact.jpg')"><div class="wrap"><h1>Contact / Order an Appraisal</h1><p>Free, no-pressure consultation about your date-of-death, estate, or other appraisal needs in San Diego and San Diego County.</p></div></section>
<section class="section"><div class="wrap contact-grid">
  <div class="contact-form-col">
    <h2>Getting Started Online Form</h2>
    <p>Complete the form as fully as possible and I'll review your needs, the property, and the available market data, then follow up with a quote. You may also call or email directly.</p>
    <form class="contact-form" action="https://www.brianward.com/api/contact" method="post">
      <div class="field"><label for="name">Name *</label><input type="text" id="name" name="name" required></div>
      <div class="field"><label for="email">Email *</label><input type="email" id="email" name="email" required></div>
      <div class="field"><label for="phone">Phone</label><input type="tel" id="phone" name="phone"></div>
      <div class="field"><label for="street-address">Street Address</label><input type="text" id="street-address" name="street-address"></div>
      <div class="field-row">
        <div class="field"><label for="city">City</label><input type="text" id="city" name="city"></div>
        <div class="field"><label for="zipcode">Zip Code</label><input type="text" id="zipcode" name="zipcode"></div>
      </div>
      <div class="field"><label for="appraisal-purpose">Appraisal Purpose *</label>
        <select id="appraisal-purpose" name="appraisal-purpose" required><option value="">- Select Appraisal Purpose -</option>
<option value="bankruptcy">Bankruptcy</option>
<option value="date-of-death">Date of Death</option>
<option value="divorce">Divorce</option>
<option value="estate">Estate</option>
<option value="tax">Tax</option>
<option value="before-buying">Before Buying</option>
<option value="before-selling">Before Selling</option>
<option value="family-transaction">Family Transaction</option>
<option value="insurance-dispute">Insurance Dispute</option>
<option value="pmi-removal">PMI Removal</option>
<option value="bonds">Bonds</option>
<option value="other">Other</option></select></div>
      <div class="field"><label for="appraisal-type">Appraisal Type</label>
        <select id="appraisal-type" name="appraisal-type"><option value="">- Select Appraisal Type -</option>
<option value="basic-desktop">Basic Desktop Appraisal &mdash; $299</option>
<option value="desktop">Desktop Appraisal &mdash; $449</option>
<option value="drive-by">Drive-By Appraisal &mdash; $575</option>
<option value="standard">Standard Appraisal &mdash; $625</option>
<option value="desktop-2-4">Desktop 2-4 Unit &mdash; $550</option>
<option value="standard-2-4">Standard 2-4 Unit &mdash; $725</option>
<option value="not-sure">Not sure &mdash; help me decide</option></select>
        <p class="field-note">Fees listed are starting prices. Complex, high-liability, or extended-travel properties may be higher. Your exact fee is quoted before you commit.</p></div>
      <div class="field"><label for="message">Additional Information</label><textarea id="message" name="message" rows="5"></textarea></div>
      <button type="submit" class="btn btn-primary">Submit Request</button>
    </form>
  </div>
  <aside class="contact-info-col">
    <h2>Contact Information</h2>
    <div class="info-block"><span class="info-label">Phone</span><a class="info-big" href="tel:{PHONE_T}">{PHONE_D}</a></div>
    <div class="info-block"><span class="info-label">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <p class="info-note">If I don't answer right away, I'm probably giving a client my full attention. Please leave a message and I'll return your call promptly &mdash; I extend the same courtesy to you.</p>
    <div class="info-block"><span class="info-label">Serving</span><p>All of San Diego County, including {serving}, and every community in between.</p></div>
  </aside>
</div></section>'''
    body+=footer(p)
    write("contact.html", body)

# ---------------- 404 ----------------
def build_404():
    p=""
    body=head(p,"Page Not Found","The page you're looking for isn't here. Return home or contact Brian Ward Appraisal for a San Diego County appraisal.",f"{BASE}/404.html",f"{BASE}/images/og-image.jpg")
    body=body.replace('<meta name="robots" content="index, follow, max-image-preview:large">','<meta name="robots" content="noindex, follow">')
    body+=f'''<section class="page-head" style="background:{GRAD.replace(",url","")}"><div class="wrap"><h1>Page Not Found</h1><p>Sorry — that page doesn't exist or has moved.</p></div></section>
<section class="section"><div class="wrap narrow center">
  <p class="lead">Let's get you back on track.</p>
  <p><a class="btn btn-primary" href="index.html">Return Home</a> <a class="btn btn-outline" href="service-area.html">Browse Service Area</a></p>
  <p>Or call <a href="tel:{PHONE_T}">{PHONE_D}</a> to speak with a certified San Diego County appraiser.</p>
</div></section>'''
    body+=footer(p)
    write("404.html", body)

# ---------------- SITEMAP / ROBOTS / LLMS / CNAME / README ----------------
def build_seo():
    urls=["index.html","appraisal-fees.html","service-area.html","faq.html","reviews.html","contact.html"]
    urls+=[f"services/{s['slug']}.html" for s in SERVICES]
    urls+=[f"areas/{s}.html" for s in ORDER]
    today="2026-07-11"
    items=""
    for u in urls:
        pri="1.0" if u=="index.html" else ("0.8" if (u.startswith("services/") or u in ("appraisal-fees.html","service-area.html","contact.html")) else "0.6")
        items+=f"  <url><loc>{BASE}/{u}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{pri}</priority></url>\n"
    sitemap=f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}</urlset>\n'
    write("sitemap.xml", sitemap)

    robots=f"""User-agent: *
Allow: /

# AI / LLM crawlers explicitly welcomed
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-Web
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Amazonbot
Allow: /
User-agent: CCBot
Allow: /

Sitemap: {BASE}/sitemap.xml
"""
    write("robots.txt", robots)

    # llms.txt
    price_lines="""- Basic Desktop: $299 — Records-based valuation with no property visit. MLS data, county records, and recent comparable sales analysis.
- Desktop Appraisal: $449 — Enhanced records review, neighborhood analysis, and detailed comparable sales study. No property visit.
- Drive-By Appraisal: $575 — Exterior-only inspection with photographs. Includes property condition notes and full market analysis.
- Standard (Single Family): $625 — Full interior and exterior inspection with detailed property photographs. Complete narrative appraisal report.
- Desktop (2–4 Unit): $550 — Multi-unit records-based valuation with separate unit analysis. No property visit.
- Standard (2–4 Unit): $725 — Multi-unit full interior and exterior inspection. Separate unit analysis and complete narrative report."""
    svc_lines="\n".join(f"- [{s['name'].replace('&amp;','&')}]({BASE}/services/{s['slug']}.html): {s['llms']}" for s in SERVICES)
    area_lines="\n".join(f"- [{AREA_NAME[s]}, CA]({BASE}/areas/{s}.html)" for s in ORDER)
    llms=f"""# Brian Ward Appraisal — San Diego Date of Death & Estate Appraiser

> California Certified Residential Real Estate Appraiser serving the City of San Diego and all of San Diego County since 2004. 20+ years of experience and 7,000+ appraisals completed. This site's lead specialty is date-of-death and other retrospective estate appraisals; it also covers divorce, bankruptcy, expert witness, pre-purchase, and pre-sale valuations. All reports comply with USPAP.

## Key Facts
- Business: Brian Ward Appraisal
- Primary / parent website: https://www.brianward.com (Brian Ward Appraisal, serving San Diego & Riverside Counties across all appraisal purposes). This site, sandiegoappraiser.pro, is the City of San Diego / San Diego County presence of the same business, led by date-of-death and estate appraisal work; brianward.com is the main, authoritative site.
- Appraiser credential: California Certified Residential Real Estate Appraiser
- Phone: {PHONE_D}
- Email: {EMAIL}
- Service area: The City of San Diego and its neighborhoods, plus all of San Diego County, California (North County coastal, North County inland, North County estates, East County, South Bay, and the accessible backcountry)
- Pricing: Residential appraisals from $299 (Basic Desktop) to $725 (Standard 2–4 Unit). Exact fee quoted before commitment.

## Pricing
{price_lines}

## Services
{svc_lines}

## Service Area (Cities & Communities)
{area_lines}

## Pages
- [Home]({BASE}/index.html)
- [Services & Fees]({BASE}/appraisal-fees.html)
- [Service Area]({BASE}/service-area.html)
- [FAQ]({BASE}/faq.html)
- [Reviews]({BASE}/reviews.html)
- [Contact]({BASE}/contact.html)
"""
    write("llms.txt", llms)
    write("CNAME", "www.sandiegoappraiser.pro\n")
    write(".gitignore", ".DS_Store\nThumbs.db\n")
    write("README.md", f"""# sandiegoappraiser.pro

Static marketing website for **Brian Ward Appraisal** — San Diego date-of-death and estate appraisal specialist, serving the City of San Diego and all of San Diego County.

- Pure static HTML/CSS/JS (no build step). Deployed via Cloudflare Pages.
- {len(SERVICES)} service pages, {len(ORDER)} city/community area pages, full SEO + structured data (JSON-LD), sitemap, robots, and llms.txt for AI inclusion.
- Sister site of the main company site, [brianward.com](https://www.brianward.com).

Contact: {PHONE_D} · {EMAIL}
""")

# ---------------- RUN ----------------
if __name__=="__main__":
    build_index()
    for s in SERVICES: build_service(s)
    for slug in ORDER: build_area(slug)
    build_fees(); build_service_area(); build_faq(); build_reviews(); build_contact(); build_404()
    build_seo()
    # count
    n=sum(len(files) for _,_,files in os.walk(OUT) for f in [0])
    total=0
    for r,d,files in os.walk(OUT):
        for f in files:
            if f.endswith(('.html','.xml','.txt','.md')): total+=1
    print("BUILD OK. HTML/xml/txt/md files:",total)
    print("services:",len(SERVICES)," areas:",len(ORDER))
