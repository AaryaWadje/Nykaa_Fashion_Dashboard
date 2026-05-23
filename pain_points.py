PAIN_POINTS = {
    "📏 Size & Fit Confusion": {
        "icon": "📏",
        "short": "Size & Fit Confusion",
        "desc": "Users return items frequently due to unclear sizing charts and no personalised size guidance.",
        "severity": "High",
        "stat": "67%",
        "stat_label": "Returns cite wrong size",
        "problem_statement": (
            "Nykaa Fashion users frequently receive incorrectly sized clothing due to the absence of "
            "personalised size recommendations and inconsistent brand sizing. This leads to a high "
            "return rate, increased logistics costs, and poor post-purchase experience that reduces "
            "repeat purchase intent."
        ),
        "research": [
            {
                "title": "App Store Reviews (3.1★ for sizing)",
                "body": (
                    "Nykaa Fashion Play Store reviews frequently mention 'size runs small', "
                    "'no consistent sizing across brands', and 'different from what the chart shows'. "
                    "Users report ordering 2 sizes to try and return one — increasing logistics costs."
                ),
            },
            {
                "title": "Industry Benchmark",
                "body": (
                    "In India's fashion e-commerce, size-related returns account for 55–70% of all returns "
                    "(Redseer 2023). Return rates for apparel are 25–35% vs 5% for electronics. "
                    "Each return costs ₹80–120 in reverse logistics."
                ),
            },
            {
                "title": "Competitive Gap",
                "body": (
                    "Myntra has 'Size Recommender' powered by 1000+ measurements. AJIO shows 'Fit Guide' by body shape. "
                    "Nykaa Fashion currently shows only a static brand-specific size chart — no personalised "
                    "recommendation or body-fit filter."
                ),
            },
        ],
        "personas": [
            {
                "icon": "👩",
                "name": "Priya Sharma",
                "role": "26 yrs · Marketing Executive · Mumbai · Mid-spender",
                "quote": (
                    '"I order 3 sizes of the same outfit every time. I know I\'ll return 2 but '
                    'I have no idea which will fit me right. It\'s frustrating and wasteful."'
                ),
                "goals": ["Find correct size on first order", "Avoid hassle of returns"],
                "frustrations": ["Inconsistent brand sizing", "No try-before-buy option"],
            },
            {
                "icon": "🧑",
                "name": "Rohan Mehta",
                "role": "32 yrs · First-time buyer · Pune · Budget-conscious",
                "quote": (
                    '"I gave up on ordering clothes online after two wrong sizes in a row. '
                    'I just go to the shop now even though it\'s further."'
                ),
                "goals": ["Trust online purchases", "Get value for money"],
                "frustrations": ["No way to verify fit", "Return process feels risky"],
            },
        ],
        "rice": [
            {"feature": "Community Size Reviews (True to size / Runs small tags)", "reach": "10M", "impact": 7, "confidence": "90%", "effort": "3 weeks", "score": 210.0},
            {"feature": "Smart Size Recommender (body measurements + order history)", "reach": "8M", "impact": 9, "confidence": "80%", "effort": "6 weeks", "score": 96.0},
            {"feature": "Standardised Indian Size Chart (Nykaa own label)", "reach": "5M", "impact": 6, "confidence": "70%", "effort": "8 weeks", "score": 26.3},
            {"feature": "AR Virtual Try-On", "reach": "3M", "impact": 10, "confidence": "50%", "effort": "24 weeks", "score": 6.3},
        ],
        "solution_name": "SizeMatch — Community + AI Size Intelligence",
        "solution_flow": [
            "User opens product",
            "Taps 'Find My Size'",
            "Inputs measurements OR selects body type",
            "Gets recommended size + confidence %",
            "Reads verified buyer size reviews",
            "Orders with confidence",
        ],
        "acceptance_criteria": [
            "Users can input height, weight, chest/waist/hip to get a recommended size",
            "Community buyers can tag reviews as 'Runs small / True to size / Runs large'",
            "System shows % of buyers who found the item true-to-size",
            "Returns tagged 'wrong size' are tracked as a guardrail metric",
            "Feature is accessible before add-to-cart on every product page",
        ],
        "north_star": "Size-related return rate (%)",
        "okrs": [
            {"objective": "Reduce returns", "key_result": "Reduce size-related return rate from 28% → 18% in 90 days"},
            {"objective": "Increase conversion", "key_result": "Increase add-to-cart rate by 12% for products with SizeMatch enabled"},
            {"objective": "Drive engagement", "key_result": "30% of buyers leave a size review within 2 weeks of delivery"},
        ],
        "guardrails": [
            "No increase in overall checkout time",
            "NPS must not drop below current baseline",
            "Return processing cost per order must not increase",
        ],
        "roadmap": [
            {"phase": "Phase 1 (Week 1–2)", "title": "Community Size Tags", "tasks": "Add 'Runs small / True to size / Runs large' tag to review flow. A/B test on top 100 SKUs."},
            {"phase": "Phase 2 (Week 3–6)", "title": "AI Size Recommender", "tasks": "Build measurement input + ML model using past order + return data. Soft-launch to 10% of users."},
            {"phase": "Phase 3 (Week 7+)", "title": "Personalised Fit Profile", "tasks": "Persistent 'My Measurements' in profile. Auto-suggest sizes across all categories."},
        ],
        "interview_qa": [
            {"q": "Tell me about a product problem you identified.", "a": "I identified that 67% of Nykaa Fashion's returns were size-related. I analysed app reviews, mapped the user journey, and found no personalised size guidance. I proposed SizeMatch — combining community review tags and a measurement-based recommender — with a success target of reducing return rate from 28% to 18%."},
            {"q": "How did you prioritise features?", "a": "I used the RICE framework. Community Size Tags scored 210 — high reach (10M), 90% confidence, only 3 weeks effort. AR Try-On scored 6.3 due to high effort and low confidence. I always lead with high-confidence, fast-to-ship wins."},
            {"q": "What metrics would you track?", "a": "North Star: size-related return rate. Secondary: add-to-cart rate on SizeMatch products, % of buyers leaving a size review. Guardrails: checkout time, NPS, and return logistics cost — ensuring we don't solve one problem while creating another."},
            {"q": "How did you validate the problem?", "a": "Three ways — qualitative (app reviews, Reddit r/IndianFashion), quantitative (Redseer benchmark: 55–70% of Indian fashion returns are size-related), and competitive analysis (Myntra + AJIO both have size solutions). This triangulation gave me confidence the problem was real and large."},
        ],
    },

    "🔍 Discovery & Personalisation Gap": {
        "icon": "🔍",
        "short": "Discovery & Personalisation Gap",
        "desc": "Users struggle to find relevant styles matching their taste, body type, and occasion.",
        "severity": "High",
        "stat": "3.2",
        "stat_label": "Avg items browsed before exit",
        "problem_statement": (
            "Nykaa Fashion users exit after browsing only 3.2 items on average (vs 7–10 on Myntra) "
            "because the platform lacks personalised style recommendations. Without a taste profile, "
            "the homepage and search results surface generic 'popular' items rather than taste-matched "
            "suggestions, reducing engagement, conversion, and retention."
        ),
        "research": [
            {
                "title": "Behavioural Data Signals",
                "body": (
                    "Users exit Nykaa Fashion after browsing only 3.2 items — well below the 7–10 range "
                    "seen on Myntra. Without style profiling, search results show generic 'popular' items "
                    "rather than taste-matched suggestions."
                ),
            },
            {
                "title": "User Feedback Patterns",
                "body": (
                    "Reviews and app feedback highlight 'can't find my style', 'results feel random', "
                    "and 'too many options but nothing fits my vibe'. This signals a relevance gap, "
                    "not a catalogue gap — the items exist but users can't surface them."
                ),
            },
            {
                "title": "Competitive Landscape",
                "body": (
                    "Myntra's 'My Fashion DNA' lets users pick style archetypes. Meesho uses social proof "
                    "and regional taste signals. AJIO has occasion-based filters. Nykaa Fashion's filters "
                    "are category-only with no style or body-type dimension."
                ),
            },
        ],
        "personas": [
            {
                "icon": "🌟",
                "name": "Sneha Iyer",
                "role": "24 yrs · Content Creator · Bengaluru · Trend-driven spender",
                "quote": '"I want Nykaa to know my vibe — boho casual, earthy tones, oversized fits. Instead I get whatever is trending for everyone.',
                "goals": ["Discover styles that match her aesthetic", "Get personalised outfit ideas"],
                "frustrations": ["Generic trending feed", "No style filter or quiz"],
            },
            {
                "icon": "👩‍💼",
                "name": "Anita Rao",
                "role": "38 yrs · HR Manager · Hyderabad · Occasion-based buyer",
                "quote": '"I only shop for weddings, office, or holidays. I wish I could say \'I need an outfit for a family wedding in December\' and get curated options."',
                "goals": ["Occasion-based outfit discovery", "Curated edits by event type"],
                "frustrations": ["No occasion filter", "Has to manually search for 'wedding outfit'"],
            },
        ],
        "rice": [
            {"feature": "Style Quiz Onboarding (5-question visual setup)", "reach": "12M", "impact": 8, "confidence": "85%", "effort": "4 weeks", "score": 204.0},
            {"feature": "Occasion-based Outfit Curation (Wedding, Office, Casual)", "reach": "9M", "impact": 7, "confidence": "80%", "effort": "5 weeks", "score": 100.8},
            {"feature": "AI 'Complete the Look' cross-sell", "reach": "15M", "impact": 6, "confidence": "75%", "effort": "8 weeks", "score": 84.4},
            {"feature": "Body-type based filter", "reach": "7M", "impact": 9, "confidence": "70%", "effort": "10 weeks", "score": 44.1},
        ],
        "solution_name": "StyleDNA — Taste-Matched Personalisation Onboarding",
        "solution_flow": [
            "New/returning user opens app",
            "Prompted: 'Let's find your style'",
            "5-question visual quiz (occasions, colours, fits)",
            "Style profile saved",
            "Homepage + search personalised",
            "'Complete the look' suggestions appear",
        ],
        "acceptance_criteria": [
            "Style quiz launches on first session (skippable, completable later in Settings)",
            "Users can update their style profile at any time",
            "Homepage hero section and 'Trending' are personalised to profile",
            "Occasion filters available at category and brand level",
            "A/B test: personalised home vs control shows >8% higher add-to-cart",
        ],
        "north_star": "Average items browsed per session (engagement depth)",
        "okrs": [
            {"objective": "Improve relevance", "key_result": "Increase avg items browsed per session from 3.2 → 6.0 in 60 days"},
            {"objective": "Drive conversion", "key_result": "Conversion rate from browse to cart 15% higher for quiz completers vs non-completers"},
            {"objective": "Increase retention", "key_result": "30-day retention for quiz completers exceeds baseline by 20%"},
        ],
        "guardrails": [
            "Catalogue diversity must not decrease (no filter bubble)",
            "Style quiz completion rate must stay above 55% to validate UX",
            "No increase in time-to-first-product-view",
        ],
        "roadmap": [
            {"phase": "Phase 1 (Week 1–3)", "title": "Style Quiz + Profile", "tasks": "Build 5-question visual onboarding quiz. Store style profile. A/B test homepage personalisation."},
            {"phase": "Phase 2 (Week 4–7)", "title": "Occasion-based Curation", "tasks": "Add Occasion filter (Wedding, Office, Casual, Festive, Travel). Map catalogue tags. Launch curated edits."},
            {"phase": "Phase 3 (Week 8+)", "title": "AI Recommendations Engine", "tasks": "Feed style profile into ML model. Real-time 'because you liked X' cards on PDP and cart page."},
        ],
        "interview_qa": [
            {"q": "Tell me about a product problem you worked on.", "a": "I analysed Nykaa Fashion's discovery funnel and found users browse only 3.2 items before exiting — a relevance problem, not a catalogue problem. I designed StyleDNA, a 5-question style quiz that creates a taste profile to personalise search, home, and recommendations. Goal: double browse depth to 6+ items per session."},
            {"q": "How did you prioritise features?", "a": "RICE: Style Quiz scored 204 — highest reach (12M users), high confidence, only 4 weeks effort. Body-type filters scored 44.1 due to complex tagging. I led with the quiz because it unlocks personalisation for everything downstream."},
            {"q": "What metrics would you track?", "a": "North Star: average items browsed per session. Also quiz completion rate, conversion for quiz completers vs not, and 30-day retention. Guardrails: no filter bubble, time-to-first-product-view must not increase."},
            {"q": "How did you validate the problem?", "a": "Competitor benchmarks (Myntra users browse 7–10 items), user feedback themes around 'can't find my style', and UX flow mapping confirmed no personalisation mechanism on Nykaa Fashion. All three signals pointed to the same gap."},
        ],
    },

    "📸 Product Image Quality Gap": {
        "icon": "📸",
        "short": "Product Image Quality Gap",
        "desc": "Static product photos don't show real fabric texture, drape, or how items look on real bodies.",
        "severity": "Medium",
        "stat": "45%",
        "stat_label": "Users abandon due to unclear visuals",
        "problem_statement": (
            "Nykaa Fashion averages only 2.1 product images per SKU — well below the industry benchmark "
            "of 5–6 — and lacks real-model or buyer-uploaded photos. This creates a trust gap that leads "
            "to 45% of PDP abandonment events and 22% of returns tagged 'not as described', directly "
            "impacting conversion rates and brand trust."
        ),
        "research": [
            {
                "title": "User Trust Barrier",
                "body": (
                    "Nearly half of abandonment events on fashion PDPs are attributed to poor visual confidence. "
                    "Users can't see drape, fabric texture, or how items look on real bodies from flat-lay "
                    "photography alone."
                ),
            },
            {
                "title": "App Review Signals",
                "body": (
                    "Reviews frequently mention 'looks different in real life', 'can't tell the fabric quality', "
                    "and 'only one angle shown'. Returns tagged 'not as described' or 'different colour/fabric' "
                    "make up ~22% of all returns."
                ),
            },
            {
                "title": "Benchmark",
                "body": (
                    "AJIO shows 4–6 angles including model close-ups. Myntra introduced 360° videos for top SKUs. "
                    "Nykaa Fashion averages 2.1 images per product — significantly below the 5–6 industry benchmark."
                ),
            },
        ],
        "personas": [
            {
                "icon": "🎨",
                "name": "Divya Krishnan",
                "role": "29 yrs · Interior Designer · Chennai · Quality-focused",
                "quote": '"I need to see the fabric up close. Is it sheer? Does it crease? One flat-lay photo tells me nothing."',
                "goals": ["Understand fabric quality before buying", "See close-up detail shots"],
                "frustrations": ["Only 1–2 images per product", "No texture or drape visibility"],
            },
            {
                "icon": "📱",
                "name": "Karan Bhatia",
                "role": "22 yrs · Student · Delhi · Deals-driven",
                "quote": '"I buy based on how it looks on a real person. Those mannequin shots are useless. Show me a real body wearing it."',
                "goals": ["See real-person model photos", "Trust product before purchasing"],
                "frustrations": ["Mannequin-only photos", "No buyer-uploaded real photos"],
            },
        ],
        "rice": [
            {"feature": "Mandate 5+ product shots + model close-ups from sellers", "reach": "20M", "impact": 8, "confidence": "90%", "effort": "4 weeks", "score": 360.0},
            {"feature": "Buyer photo reviews ('Show your delivery')", "reach": "18M", "impact": 7, "confidence": "85%", "effort": "3 weeks", "score": 357.0},
            {"feature": "Video unboxing / live product view", "reach": "8M", "impact": 9, "confidence": "60%", "effort": "16 weeks", "score": 27.0},
            {"feature": "AR try-on overlay", "reach": "4M", "impact": 10, "confidence": "40%", "effort": "26 weeks", "score": 6.2},
        ],
        "solution_name": "TrueView — Seller Image Standards + Buyer Photo Reviews",
        "solution_flow": [
            "Seller uploads product",
            "Checklist: 5 image types required",
            "Listing published with complete gallery",
            "Buyer receives order",
            "Prompted: 'Share how it looks on you'",
            "Photo tagged as verified buyer",
            "Future buyers see real-person visuals",
        ],
        "acceptance_criteria": [
            "Sellers must provide minimum 5 images: front, back, close-up fabric, model view, detail shot",
            "New listings without 5+ images are not shown in discovery until complete",
            "Post-delivery push prompts buyer to upload a real-wear photo",
            "Verified buyer photos appear as a separate carousel on PDP",
            "Seller image score visible to buyers as a trust indicator",
        ],
        "north_star": "PDP-to-cart conversion rate",
        "okrs": [
            {"objective": "Improve trust", "key_result": "Reduce 'not as described' returns from 22% → 12% within 90 days"},
            {"objective": "Drive conversion", "key_result": "Products with 5+ images show 20% higher PDP-to-cart rate vs 1–2 image products"},
            {"objective": "Build community content", "key_result": "25% of delivered orders receive a buyer photo within 6 weeks of launch"},
        ],
        "guardrails": [
            "Seller churn rate must not increase (monitor for dropoff if image requirements are too strict)",
            "Catalogue listing speed should not decrease by more than 15%",
        ],
        "roadmap": [
            {"phase": "Phase 1 (Week 1–2)", "title": "Buyer Photo Reviews", "tasks": "Add photo upload to review flow. Post-delivery push nudge. A/B test on 50 top SKUs."},
            {"phase": "Phase 2 (Week 3–5)", "title": "Seller Image Standards", "tasks": "Enforce 5-image minimum for new listings. Provide free photography guide toolkit to sellers."},
            {"phase": "Phase 3 (Week 6+)", "title": "Image Quality Score", "tasks": "ML-based image quality scoring. Deprioritise low-quality listings in search ranking."},
        ],
        "interview_qa": [
            {"q": "Tell me about a product problem you identified.", "a": "45% of Nykaa Fashion abandonment was linked to poor visuals — only 2.1 images per product vs the industry benchmark of 5–6. I built TrueView: enforcing seller image standards (5+ image types required) and adding post-delivery buyer photo reviews to build real-person visual trust on PDPs."},
            {"q": "How did you prioritise?", "a": "RICE showed Seller Image Standard mandate scored 360 and Buyer Photo Reviews scored 357 — both high because of massive reach and high confidence. Both took less than 4 weeks. I prioritised these over AR Try-On (score: 6.2) where effort was exponentially higher."},
            {"q": "How do you handle sellers who resist the image requirements?", "a": "I'd frame it as a conversion benefit — more images = higher conversion = more revenue for them. I'd provide a free photography guide and grace period before enforcement, and monitor seller churn as a guardrail metric to catch negative impact early."},
            {"q": "What is your go-to-market plan?", "a": "Phase 1: soft launch buyer photo reviews — zero seller friction, immediate UGC benefit. Phase 2: enforce 5-image standard on new listings only (no retroactive enforcement). Phase 3: ML quality scoring to demote poor-image listings in search — creating positive incentive loop."},
        ],
    },

    "📦 Post-Purchase Experience": {
        "icon": "📦",
        "short": "Post-Purchase Experience",
        "desc": "Returns, exchanges, and delivery tracking are fragmented. Users feel abandoned after purchase.",
        "severity": "Medium",
        "stat": "38%",
        "stat_label": "Users don't repurchase after a bad return",
        "problem_statement": (
            "Nykaa Fashion loses 38% of buyers permanently after one bad return experience — above the "
            "22% industry average. The return flow requires 6+ taps with no exchange option, "
            "minimal tracking (only 3 states), and no proactive delay communication. This creates "
            "anxiety, high support ticket volume, and permanently reduces lifetime value."
        ),
        "research": [
            {
                "title": "Retention Data",
                "body": (
                    "Post-purchase experience is the single biggest driver of lifetime value in fashion e-commerce. "
                    "Nykaa Fashion loses 38% of buyers permanently after one bad return — significantly above "
                    "the industry average of 22%."
                ),
            },
            {
                "title": "Pain Points in the Journey",
                "body": (
                    "Return initiation requires 6+ taps. Exchange is not available for most items (refund only). "
                    "Delivery tracking shows only 3 states (dispatched, in transit, delivered) with no granular "
                    "updates. No proactive communication for delays."
                ),
            },
            {
                "title": "Trust Gap",
                "body": (
                    "Users report anxiety about whether returns are received and refunds processed. "
                    "Support chat has avg 4-hour first response. No self-serve resolution for common issues "
                    "like partial delivery or delayed return pickup."
                ),
            },
        ],
        "personas": [
            {
                "icon": "😤",
                "name": "Meera Sinha",
                "role": "31 yrs · Teacher · Bhopal · Value-conscious",
                "quote": '"I initiated a return 3 weeks ago. I\'ve called 3 times, chatted twice. Still no refund. This was my last order from Nykaa Fashion."',
                "goals": ["Transparent return tracking", "Fast refund processing"],
                "frustrations": ["No return status visibility", "Slow support response"],
            },
            {
                "icon": "🏃",
                "name": "Arjun Kapoor",
                "role": "27 yrs · Sales professional · Gurgaon · Frequent buyer",
                "quote": '"I want to exchange a shirt for a different size but there\'s no exchange option. Why is return+re-order the only way? That\'s two hassles not one."',
                "goals": ["Direct size exchange without re-ordering", "Fast resolution"],
                "frustrations": ["No exchange option", "Return + re-order double friction"],
            },
        ],
        "rice": [
            {"feature": "Proactive delay SMS/push notifications", "reach": "20M", "impact": 6, "confidence": "95%", "effort": "2 weeks", "score": 570.0},
            {"feature": "Real-time return tracking (5-stage: Pickup → Received → Refund)", "reach": "18M", "impact": 7, "confidence": "90%", "effort": "4 weeks", "score": 283.5},
            {"feature": "One-tap return initiation + instant pickup scheduling", "reach": "15M", "impact": 9, "confidence": "85%", "effort": "5 weeks", "score": 229.5},
            {"feature": "Direct exchange (no return + re-order flow)", "reach": "10M", "impact": 8, "confidence": "70%", "effort": "10 weeks", "score": 56.0},
        ],
        "solution_name": "NykaaReturn Pro — Frictionless Post-Purchase",
        "solution_flow": [
            "Order delivered",
            "One-tap 'Return / Exchange' in Orders",
            "Select reason → refund or exchange size",
            "Pickup scheduled in <2 min",
            "Real-time 5-stage tracker updates",
            "Refund or exchange dispatched",
            "Push notification confirms completion",
        ],
        "acceptance_criteria": [
            "Return initiation completable in 3 taps or fewer",
            "Exchange option available for all clothing/footwear SKUs (size swap only)",
            "Return tracker: Requested → Pickup Scheduled → Picked Up → Received → Refund Processed",
            "Proactive SMS + push for any delivery delay >24 hours",
            "Refund SLA displayed at initiation: '₹ will be credited by [date]'",
        ],
        "north_star": "90-day repeat purchase rate after a return event",
        "okrs": [
            {"objective": "Retain users", "key_result": "Increase 90-day repeat purchase rate post-return from 62% → 80% within 6 months"},
            {"objective": "Reduce effort", "key_result": "Reduce return initiation from avg 6 taps → 3 taps; measure via analytics"},
            {"objective": "Build trust", "key_result": "Increase post-purchase cohort NPS by 25 points"},
        ],
        "guardrails": [
            "Return rate must not increase (feature must not incentivise fraudulent returns)",
            "Refund processing cost per return must not increase",
            "Customer support ticket volume for returns should decrease",
        ],
        "roadmap": [
            {"phase": "Phase 1 (Week 1–2)", "title": "Proactive Delay Notifications", "tasks": "Trigger SMS + push for delays >24h. Zero engineering risk, immediate NPS impact."},
            {"phase": "Phase 2 (Week 3–6)", "title": "One-tap Return + Real-time Tracker", "tasks": "Redesign return flow. Integrate with courier API for 5-stage tracking. A/B test vs old flow."},
            {"phase": "Phase 3 (Week 7+)", "title": "Direct Exchange Flow", "tasks": "Build size-swap exchange without re-order. Pilot on top 500 SKUs. Roll out if CSAT > 4.2."},
        ],
        "interview_qa": [
            {"q": "Tell me about a product problem you worked on.", "a": "Nykaa Fashion loses 38% of customers permanently after one bad return — above industry average. The return flow required 6+ taps, no exchange option, and minimal tracking. I designed NykaaReturn Pro: one-tap return, direct exchange, 5-stage tracking, and proactive delay notifications. North Star: improve repeat purchase rate post-return from 62% to 80%."},
            {"q": "How did you decide what to build first?", "a": "RICE analysis. Proactive Delay Notifications scored 570 — highest of all options — because 20M users are affected, 95% confidence, and only 2 weeks to build. It was a clear quick win to sequence before the larger one-tap return redesign (score: 229.5 but more effort)."},
            {"q": "How do you prevent the easy-return feature from increasing fraud?", "a": "Exchange option is size-swap only, not open-ended. I'd set a guardrail metric tracking return rate — if it spikes, investigate. Photo upload required for 'wrong item' claims. Repeat returners flagged for review. PM work always involves balancing UX with business health."},
            {"q": "What's the biggest risk in this project?", "a": "Seller and courier API integration for real-time tracking can be delayed. My mitigation: Phase 1 (notifications) requires zero API changes — it's a pure push trigger. If Phase 2 integration is delayed, users still benefit from Phase 1 immediately. Always ship value early rather than waiting for the full solution."},
        ],
    },
}
