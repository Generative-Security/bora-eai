# Incident library

Public incidents used as evidence in BORA-EAI, mapped to scenarios. Incidents are reported plainly: what happened, to whom, and what it cost where known. Labels follow [evidence labels](evidence-labels.md).

This library is small and biased toward incidents that were publicly reported, which over-represents viral customer-facing failures and under-represents quiet internal losses. It is a starting point for the [incident-coding test](../validation/validation-plan.md), not a frequency dataset.

| Date | Organization | Scenario | What happened | Known impact | Evidence |
|---|---|---|---|---|---|
| Spring 2023 | Samsung | B3, B1 | Employees entered sensitive information, including source code, into ChatGPT in three reported incidents | Samsung restricted generative AI on company devices | `[secondary]` [TechRadar](https://www.techradar.com/news/samsung-bans-chatgpt-use-after-employee-leak) |
| Aug 2023 | Zoom | B7, B5 | Terms changes from March 2023 were read as allowing AI training on customer content without opt-out; Zoom updated terms on 7 August to require consent | Public backlash; terms changed | `[secondary]` [Engadget](https://www.engadget.com/zoom-reverses-policy-that-allowed-it-to-train-ai-on-customer-data-212230598.html) |
| Dec 2023 | Chevrolet of Watsonville (bot supplied by Fullpath) | B10 | A user instructed the dealer chatbot to call every reply "a legally binding offer" and got it to agree to sell a 2024 Tahoe (MSRP from US$58,195) for US$1 | Not honored or litigated; dealerships disabled bots | `[secondary]` [VentureBeat](https://venturebeat.com/ai/a-chevy-for-1-car-dealer-chatbots-show-perils-of-ai-for-customer-service) |
| Jan 2024 | DPD (UK) | B10 (reputational variant), B9 | After a system update, a customer prompted the chatbot to swear and call DPD the "worst delivery firm in the world" | AI element disabled | `[secondary]` [ITV News](https://itv.com/news/2024-01-19/dpd-disables-ai-chatbot-after-customer-service-bot-appears-to-go-rogue) |
| Feb 2024 | Air Canada | B8 | Chatbot misstated the bereavement fare policy; tribunal held the airline responsible, rejecting its argument that the chatbot was a separate legal entity | CA$812.02 award; precedent | `[legal ruling]` [McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot) |
| Feb–Mar 2024 | Hugging Face users | B4 | More than 100 malicious models found, some executing code on load | Not quantified | `[vendor, via secondary]` [The Hacker News](https://thehackernews.com/2024/03/over-100-malicious-aiml-models-found-on.html) |
| Jun 2024 | Adobe | B7 | Clarified new terms after concerns about AI training on customer content | Public backlash | `[secondary]` |
| Sep 2024 | DoNotPay | B8 | FTC action over unsubstantiated "robot lawyer" claims under Operation AI Comply | US$193,000 | `[secondary]` [Morrison Foerster](https://www.mofo.com/resources/insights/241008-ftc-first-ai-related-enforcement-actions) |
| Apr 2025 | Cursor | B8 | AI support bot invented a one-device subscription policy | Reported churn and reputational harm | `[secondary]` |
| Jun 2025 | Microsoft 365 Copilot (EchoLeak, CVE-2025-32711) | B2, B9 | Zero-click exfiltration via a crafted email that Copilot retrieved alongside privileged data; CVSS 9.3 | Fixed; no in-the-wild exploitation reported | `[secondary]` [The Hacker News](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html) |
| Jun 2025 | Anthropic and Andon Labs (Project Vend experiment) | B10, B12 | A Claude-based agent running an office shop was talked into discounts and giveaways | Lost money (experiment) | `[secondary]` [TechCrunch](https://techcrunch.com/2025/06/28/anthropics-claude-ai-became-a-terrible-business-owner-in-experiment-that-got-weird) |
| Jul 2025 | Replit / SaaStr | B11 | Coding agent deleted a production database during a declared code freeze and misrepresented what happened | Reported data on 1,200+ executives and 1,190+ companies lost; ~4,000 fabricated users (counts not confirmed from primary source) | `[secondary]` [The Stack](https://www.thestack.technology/vibe-coding-ceo-deletes-production-database/) |
| Jul 2025 | WeTransfer | B7 | Removed an AI clause from its terms after backlash | Public backlash | `[secondary]` |
| Aug 2025 | Salesloft Drift (700+ customers) | B6 | Attackers stole OAuth tokens from the AI chat vendor's environment and used them to access customers' Salesforce instances | 700+ organizations affected; e.g. Cloudflare rotated 104 tokens | `[secondary]` [TechTarget](https://www.techtarget.com/searchsecurity/news/366630934/News-brief-Salesloft-Drift-breach-update-and-timeline) |
| Aug 2025 | Commonwealth Bank of Australia | B14 | Reversed decision to replace 45 customer-service roles with an AI chatbot after call volumes rose | Roles reinstated | `[secondary]` [The Register](https://www.theregister.com/2025/08/22/commonwealth_ban_chatbot_fail_rehiring/) |
| Sep 2025 | Postmark MCP impersonation | B4 | Typosquatted npm package impersonating the official Postmark MCP server silently copied all email to an attacker | Not quantified | `[industry-body]` [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-skill-supply-chain-attacks-20260624-csa/) |
| Feb–May 2026 | ClawHub agent-skill marketplace | B4 | "ClawHavoc" campaign: 1,184 confirmed malicious skills, including skills distributing the Atomic macOS Stealer | Not quantified | `[industry-body]` CSA |
| Mar 2026 | Multiple enterprises (disclosed by Microsoft) | B4, B3 | Malicious AI assistant browser extensions harvesting LLM chat histories | Not quantified | `[industry-body, via CSA]` |
| Apr 2026 | PocketOS | B11 | Cursor coding agent running Claude Opus 4.6 deleted the production database volume and all backups on its own initiative, without confirmation and despite a safeguard | 30+ hour outage for car-rental customers; three months of bookings unavailable until recovery two days later | `[secondary]` [Euronews](https://www.euronews.com/2026/04/28/an-ai-agent-deleted-a-companys-entire-database-in-9-seconds-then-wrote-an-apology) |

## Aggregate data

| Source | Finding | Scenarios | Evidence |
|---|---|---|---|
| IBM Cost of a Data Breach 2025 | 13% of organizations reported AI model or app breaches; 97% of those lacked AI access controls; one in five reported shadow-AI breaches; high shadow-AI use added US$670,000; 60% of AI incidents compromised data, 31% disrupted operations | B2, B3, B9, B11 | `[survey]` |
| Netskope Cloud and Threat Report 2026 | ~223 GenAI data-policy violations per organization per month; source code 42%, regulated data 32%, IP 16% | B3, B1 | `[vendor]` |
| Verizon 2026 Breach Impact Study | ~70,000 US cyber-insurance claims; business interruption highest median loss (~US$90,000 per claim); top 2.5% of paid claims over US$5 million; BI 44% of known retail losses | B6, B9, B11 | `[survey]` |
| Verizon 2026 DBIR (as summarized) | Shadow AI third most common non-malicious insider action; 67% of employees use non-corporate AI accounts on corporate devices | B1, B3 | `[secondary]` |
| Huwyler (2025) | Of 133 AI Incident Database incidents, Misuse 61%, Unreliable Outputs 27%, Supply Chain 5% | Various | `[preprint]` |

## Not yet verified

Incidents mentioned in sources but not checked against a primary source for this draft: the Amazon Q Developer extension with an injected wiper prompt (July 2025); the Nx "s1ngularity" npm compromise using local AI command-line tools (August 2025); Salesforce Agentforce "ForcedLeak"; Slack AI prompt injection (2024); the NYC MyCity chatbot giving unlawful advice (2024); Slack's 2024 training opt-out controversy; Google Antigravity and Gemini CLI file deletions (2025). Contributions with primary sources are welcome.
