SCENARIOS = [
    # ------------------------------------------------------------------ 1
    {
        "id": 1,
        "intent": "Follow up after a job interview",
        "facts": (
            "Interview was on Wednesday with hiring manager shreya Park; "
            "role: Senior Data Analyst; "
            "discussed experience with Python and Tableau; "
            "company: VertexAI Solutions; "
            "expressed interest in joining the analytics team"
        ),
        "tone": "Professional, grateful, confident",
        "human_reference": """Subject: Thank You – Senior Data Analyst Interview

Dear shreya,

Thank you so much for taking the time to meet with me on Wednesday to discuss the Senior Data Analyst role at VertexAI Solutions. It was a pleasure speaking with you and learning more about the team's work.

Our conversation reinforced my enthusiasm for the position. I particularly enjoyed discussing how my experience with Python and Tableau aligns with the analytics team's current projects, and I left feeling even more excited about the potential to contribute.

I remain very interested in joining VertexAI Solutions and am confident that my background would allow me to make a meaningful impact from day one. Please don't hesitate to reach out if you need any additional information.

I look forward to hearing from you regarding the next steps.

Best regards,
[Your Name]"""
    },

    # ------------------------------------------------------------------ 2
    {
        "id": 2,
        "intent": "Request a refund for a defective product",
        "facts": (
            "Product: Bluetooth headphones Model X200; "
            "purchased on March 3rd; "
            "order number: ORD-48291; "
            "defect: left ear cup stopped working after 5 days; "
            "requesting full refund of $149"
        ),
        "tone": "Firm, polite, factual",
        "human_reference": """Subject: Refund Request – Defective Bluetooth Headphones (Order #ORD-48291)

Dear Customer Support Team,

I am writing to formally request a full refund for a defective product I recently purchased.

On March 3rd, I ordered the Bluetooth Headphones Model X200 (Order #ORD-48291) for $149. Unfortunately, within just five days of use, the left ear cup completely stopped functioning, rendering the product unusable.

Given that this is a clear manufacturing defect and the item is well within the return window, I believe a full refund of $149 is the appropriate resolution.

Please advise on the return process and confirm the timeline for the refund to be processed. I am happy to return the product upon receiving a prepaid shipping label.

Thank you for your prompt attention to this matter.

Sincerely,
[Your Name]"""
    },

    # ------------------------------------------------------------------ 3
    {
        "id": 3,
        "intent": "Invite a keynote speaker to a conference",
        "facts": (
            "Conference: TechForward Summit 2025; "
            "date: October 14–15, 2025; "
            "location: Chicago, IL; "
            "speaker's expertise: AI ethics; "
            "expected audience: 800 tech professionals; "
            "honorarium offered: $3,000 + travel covered"
        ),
        "tone": "Formal, flattering, persuasive",
        "human_reference": """Subject: Keynote Speaker Invitation – TechForward Summit 2025

Dear [Speaker's Name],

I hope this message finds you well. I am reaching out on behalf of TechForward Summit 2025 to extend a formal invitation for you to join us as a keynote speaker.

Your thought leadership in AI ethics is highly regarded across the technology community, and we believe your insights would profoundly resonate with our audience. The summit will take place on October 14–15, 2025, in Chicago, IL, and we are expecting over 800 senior tech professionals, executives, and innovators.

We would be honored to have you share your expertise on a topic of your choosing within the AI ethics space. To support your participation, we are pleased to offer an honorarium of $3,000, with all travel and accommodation expenses fully covered.

We would love to discuss this opportunity further at your convenience and accommodate any scheduling preferences you may have.

Thank you for considering this invitation. We hope to welcome you to Chicago this October.

Warm regards,
[Your Name]
[Title, Organization]"""
    },

    # ------------------------------------------------------------------ 4
    {
        "id": 4,
        "intent": "Notify a team about an urgent system outage",
        "facts": (
            "System affected: payment processing API; "
            "outage started: 2:15 PM EST today; "
            "engineering team is investigating; "
            "estimated resolution: 4 hours; "
            "workaround available: manual invoice processing via admin panel; "
            "contact for updates: devops@company.com"
        ),
        "tone": "Urgent, clear, reassuring",
        "human_reference": """Subject: [URGENT] Payment Processing API Outage – Active Investigation

Team,

Please be aware that our payment processing API has been experiencing an outage since 2:15 PM EST today.

Our engineering team is actively investigating the root cause and we estimate a resolution within approximately 4 hours. We understand the impact this may have on ongoing transactions and are treating this as our top priority.

In the meantime, a workaround is available: manual invoice processing can be completed through the admin panel. Please use this option for any time-sensitive transactions.

For live updates, please monitor communications from devops@company.com. We will send status updates every 30 minutes until the issue is fully resolved.

We apologize for the disruption and appreciate your patience as we work to restore full service as quickly as possible.

[Your Name]
DevOps Team"""
    },

    # ------------------------------------------------------------------ 5
    {
        "id": 5,
        "intent": "Negotiate a freelance contract rate increase",
        "facts": (
            "Current rate: $75/hr; "
            "requesting rate: $95/hr; "
            "worked with client for 18 months; "
            "delivered 3 major projects on time; "
            "market research shows average rate for similar skills is $90–$110/hr; "
            "increase to take effect from next contract renewal"
        ),
        "tone": "Confident, respectful, data-driven",
        "human_reference": """Subject: Rate Adjustment Proposal for Upcoming Contract Renewal

Dear [Client's Name],

I hope you're doing well. As our contract renewal approaches, I wanted to take a moment to discuss an adjustment to my hourly rate and provide full context for my request.

Over the past 18 months, I've had the pleasure of delivering three major projects on time and to a high standard, and I'm proud of the results we've achieved together. At the same time, I've conducted recent market research and found that the average rate for professionals with my skill set currently falls between $90 and $110 per hour.

With this in mind, I am proposing a rate adjustment from $75/hr to $95/hr, effective from our next contract renewal. I believe this reflects both the market standard and the consistent value I've delivered to your business.

I genuinely value our working relationship and hope we can continue it under terms that reflect the quality of the collaboration. I'm happy to discuss this at your convenience.

Thank you for your continued partnership.

Best regards,
[Your Name]"""
    },

    # ------------------------------------------------------------------ 6
    {
        "id": 6,
        "intent": "Apologize for missing an important deadline",
        "facts": (
            "Missed deadline: Q2 financial report due June 30; "
            "submitted July 3 (3 days late); "
            "reason: unexpected illness; "
            "report is now complete and attached; "
            "commitment: will implement a buffer system to prevent recurrence"
        ),
        "tone": "Sincere, accountable, professional",
        "human_reference": """Subject: Apology for Late Submission – Q2 Financial Report

Dear [Manager's Name],

I want to sincerely apologize for submitting the Q2 Financial Report three days past the June 30 deadline. I understand that timely reporting is critical, and I take full accountability for the delay.

The primary cause was an unexpected illness that impaired my productivity during the final days of the reporting period. While this was unforeseen, I recognize it is my responsibility to have contingency measures in place.

I am pleased to share that the report is now fully complete and has been attached to this email for your review. I have thoroughly reviewed it to ensure accuracy and completeness despite the compressed timeline.

Going forward, I am implementing a personal buffer system — building in a 48-hour internal deadline ahead of all external due dates — to ensure this does not happen again. I am committed to maintaining the reliability you have come to expect from me.

Thank you for your understanding.

Respectfully,
[Your Name]"""
    },

    # ------------------------------------------------------------------ 7
    {
        "id": 7,
        "intent": "Pitch a business partnership",
        "facts": (
            "Our company: BrightPath Marketing; "
            "potential partner: Zenova Analytics; "
            "synergy: Zenova's data tools + BrightPath's creative services = full-stack offering; "
            "proposed: co-branded campaign for Q4 2025; "
            "mutual benefit: access to each other's client bases (BrightPath: 200+ SMB clients)"
        ),
        "tone": "Enthusiastic, professional, value-focused",
        "human_reference": """Subject: Partnership Opportunity: BrightPath Marketing x Zenova Analytics

Dear [Zenova Contact's Name],

I'm reaching out because I see a compelling partnership opportunity between BrightPath Marketing and Zenova Analytics — one that I believe could unlock significant value for both organizations.

At BrightPath, we specialize in creative marketing services and have built a network of over 200 SMB clients who trust us for growth-focused campaigns. Zenova brings powerful data and analytics tools to the table. Together, we could offer a truly full-stack solution — data-driven creative strategy — that neither of us currently provides alone.

I'd love to explore a co-branded campaign initiative for Q4 2025 as a starting point. This would give both teams an opportunity to collaborate, test the synergy, and demonstrate joint value to our respective client bases.

Beyond the immediate opportunity, there's a real chance to grow together by cross-introducing our clients — an organic and low-cost path to expansion for both sides.

I'd welcome a 30-minute call to explore whether this vision aligns with Zenova's direction. Would you be open to connecting this week or next?

Looking forward to hearing from you.

Warm regards,
[Your Name]
BrightPath Marketing"""
    },

    # ------------------------------------------------------------------ 8
    {
        "id": 8,
        "intent": "Request a letter of recommendation",
        "facts": (
            "Applying to: MBA program at Wharton School; "
            "deadline: December 1; "
            "recommender: former supervisor Dr. Alan White; "
            "worked together for 2 years at GreenBridge Consulting; "
            "key projects to highlight: led $2M infrastructure project; "
            "resume and personal statement attached"
        ),
        "tone": "Warm, respectful, considerate",
        "human_reference": """Subject: Request for MBA Recommendation Letter – Wharton Application

Dear Dr. White,

I hope you're doing well. I am reaching out with a heartfelt request — I am applying to the MBA program at the Wharton School, and I can think of no one I would more gratefully ask for a letter of recommendation than you.

Our two years working together at GreenBridge Consulting were formative for me, and I believe you have a unique perspective on my professional growth. In particular, I hope you might speak to our collaboration on the $2M infrastructure project, which I feel represents some of my strongest work in leadership and execution.

The application deadline is December 1, so I would be grateful if you were able to submit the letter by November 25 to allow some buffer. To make the process as easy as possible, I've attached my updated resume and personal statement so you have full context.

I completely understand if your schedule doesn't allow for this commitment, and there is absolutely no obligation. But if you're willing, it would truly mean a great deal to me.

Thank you so much for considering this, Dr. White.

Warmly,
[Your Name]"""
    },

    # ------------------------------------------------------------------ 9
    {
        "id": 9,
        "intent": "Announce a company policy change",
        "facts": (
            "Policy: remote work policy; "
            "change: moving from fully remote to hybrid (3 days in office); "
            "effective date: September 1; "
            "office days: Tuesday, Wednesday, Thursday; "
            "reason: collaboration and culture-building; "
            "HR contact for questions: hr@company.com"
        ),
        "tone": "Authoritative, empathetic, clear",
        "human_reference": """Subject: Important Update: New Hybrid Work Policy Effective September 1

Dear Team,

I want to share an important update regarding our remote work policy that will take effect on September 1st.

After careful consideration, we will be transitioning to a hybrid work model. Beginning September 1, all team members will be expected to work from the office on Tuesdays, Wednesdays, and Thursdays, with the flexibility to work remotely on Mondays and Fridays.

This change is driven by our commitment to fostering stronger collaboration and a vibrant team culture — two things that we believe are best nurtured through regular in-person connection. We have truly valued the flexibility of the past few years, and we want to thank everyone for their adaptability and dedication during that time.

We recognize that this represents a significant change for many of you, and we are committed to making the transition as smooth as possible. If you have any questions or need to discuss specific circumstances, please reach out to our HR team at hr@company.com.

Thank you for your continued commitment to making this a great place to work.

[Your Name]
[Title]"""
    },

    # ------------------------------------------------------------------ 10
    {
        "id": 10,
        "intent": "Thank a mentor after receiving career guidance",
        "facts": (
            "Mentor: Professor Diane Torres; "
            "advice received: pursue product management over software engineering; "
            "outcome: accepted a PM role at Stripe; "
            "start date: next Monday; "
            "have known mentor for 3 years since undergrad"
        ),
        "tone": "Personal, warm, deeply grateful",
        "human_reference": """Subject: Thank You, Professor Torres — I Got the Role at Stripe

Dear Professor Torres,

I have been waiting for the right moment to write this email, and I'm delighted to say that moment has arrived: I've officially accepted a Product Management role at Stripe, and I start next Monday!

I wanted you to be among the first to know because, in many ways, this outcome is a direct result of your guidance. When you encouraged me to pursue product management over software engineering — a path I hadn't fully considered — I was genuinely uncertain. Your belief in my ability to see the bigger picture gave me the confidence to make that pivot.

It's hard to believe it's been three years since we first connected during my undergrad. You've been a constant source of encouragement and honest counsel throughout, and that has meant more to me than I can easily put into words.

I would love to stay in touch and share how the journey unfolds. If you're ever in San Francisco, I'd be honored to treat you to coffee or dinner.

Thank you, truly, for helping shape the direction of my career.

With deep gratitude,
[Your Name]"""
    },
]
