# Financial Infrastructure Architecture

**Status:** PROPOSED — FOR REVIEW  
**Project context:** Paragon-Reborn internal research/design-training lab supporting Veiled Dominion  
**Last reviewed:** 2026-09-21

## Purpose

This document defines a proposed separation between:

1. project-level financial activity and transparency;
2. payment/treasury rails;
3. administrative and legal records.

It is an architecture proposal, not accounting, tax, or legal advice.

## System boundaries

| Layer | System | Primary responsibility |
|---|---|---|
| 🪁 Lore | OneDrive | Canon, lore, contributor material |
| ⚙️ Technical | Google Drive | Technical source of truth: code, specifications, systems design |
| 🗄️ Administrative | iCloud | Contracts, rights, invoices, tax/legal records, private supporting documentation |
| 💰 Financial activity | Open Collective | Contributions, budgets, expenses, reimbursements, project transaction activity, and transparency where appropriate |
| 🏦 Money movement / multi-currency | Wise Business | Receiving supported bank transfers, holding/converting currencies, and making bank-style payouts |
| 💳 Customer payment / card checkout | PayPal Business | Customer-facing payment acceptance, invoices, payment links, and other merchant/payment flows where appropriate |
| 🎧 Audio | Dropbox | Raw/production audio assets |
| 🔬 Research | Paragon-Reborn | Internal research, analysis, design experiments, review, and handoff |

## Core principle

**Do not make one platform do every financial job.**

Open Collective is the project-activity layer. Wise is a money-movement/multi-currency rail. PayPal is primarily a payment-acceptance and payout rail. iCloud is the administrative evidence archive.

A transaction should have one authoritative project-level record even if multiple services touch the money.

## Proposed flow

### Community/project funding

Contributor or sponsor  
→ **Open Collective**  
→ project budget / transaction record  
→ approved project expense  
→ **Wise or PayPal payout**  
→ contributor/vendor

Open Collective currently supports contributions through payment methods including PayPal, and its current Organization plans list both Wise and PayPal payouts. citeturn1search0turn1search1

### Commercial customer payment

Customer  
→ **PayPal Business** (where PayPal is the selected payment method)  
→ appropriate business financial account / treasury rail  
→ **Wise Business** when its multi-currency or international-payment capabilities are useful  
→ accounting/administrative records

PayPal Business supports invoices, payment links, cards, PayPal/Venmo and other payment methods; Wise Business supports receiving, holding, converting and sending funds in multiple currencies. citeturn0search2turn0search13turn0search4

The exact commercial flow must be determined after the legal/entity structure is established.

## PayPal's role

PayPal should **not** be treated as the master ledger.

It can occupy two different roles:

### 1. Open Collective payment processor

Open Collective can use PayPal as a contribution/payment processor. In that case, the Open Collective transaction remains the project-level record and PayPal is the payment rail underneath it. Open Collective's terms identify PayPal, Stripe, Wise and other providers as third-party payment processors used by Hosts. citeturn1search3

### 2. Independent commercial payment channel

For commercial work, a separate PayPal Business account can be used for customer-facing invoices, payment links, or checkout. PayPal's current business invoicing tools support tracking invoices and payments and offer multiple customer payment methods. citeturn0search2turn0search13

Those two roles should not be conflated.

## Wise's role

Wise is best treated as **money movement and multi-currency infrastructure**, not the project's canonical activity ledger.

Wise Business currently supports business payments, receiving money, holding 40+ currencies, currency conversion, and international transfers. Its U.S. business pricing also distinguishes domestic receiving from wire/SWIFT receiving fees. citeturn0search4turn0search5

Open Collective also lists Wise as a payout option for Organizations, so Wise can sit downstream of approved project expenses where that arrangement is available. citeturn1search1

## Financial classification

Before money moves, classify the activity:

- community contribution
- sponsorship
- grant/funding
- project expense
- contributor reimbursement
- contractor/vendor payment
- commercial sale
- licensing/IP revenue
- royalty or rights-related payment
- other

**Classification determines the appropriate financial path.**

Do not assume that every category belongs in Open Collective, PayPal, or Wise.

## Commercial vs. community boundary

The architecture should preserve a clear distinction between:

**Community/project activity**
- community contributions
- project sponsorship
- grants
- approved project expenses
- community-facing programming

and

**Commercial/proprietary activity**
- commercial sales
- licensing
- IP exploitation
- royalties
- commercial services
- other revenue belonging to a proprietary business structure

Whether a particular stream should run through Open Collective depends on the eventual legal entity, ownership, fiscal-host arrangement, contracts, and accounting requirements. It is **not** established here as a universal Open Collective rule.

## Administrative evidence

For every material transaction, retain the supporting evidence in the administrative system as appropriate:

- contract or agreement
- invoice
- receipt
- tax documentation
- ownership/rights documentation
- approval record
- relevant correspondence
- reconciliation evidence

The financial platform should record the transaction; iCloud should retain the underlying administrative evidence when that evidence belongs there.

## Reconciliation rule

Do not count a payment twice merely because it appears in multiple systems.

Example:

**$1,000 customer payment**
- PayPal: payment received
- Wise: $1,000 transferred/converted, if used
- financial ledger: **one $1,000 receipt**, plus separately recorded fees/conversion costs
- iCloud: invoice + agreement + supporting documentation

The systems are different views of the same economic event.

## When to build this

### Build now — but dry-run first

The project is at the point where the **architecture, classification system, chart of accounts, transaction IDs, approval workflow, and reconciliation procedure** should be designed.

Do **not** begin moving real money merely because the architecture exists.

### Activate before the first real external transaction

Before accepting the first real contribution, sponsorship, grant, commercial payment, or reimbursable expense:

1. establish who legally owns/controls the relevant funds;
2. decide whether the activity belongs in Open Collective, a business financial account, or another structure;
3. establish the relevant Wise and/or PayPal Business account under the correct owner;
4. establish the administrative evidence workflow;
5. test reconciliation;
6. document the first live transaction end-to-end.

### Then review

After the first small set of real transactions, review:

- fees
- payment failures
- reconciliation workload
- currency conversion
- payout timing
- documentation requirements
- privacy/public-transparency boundaries
- whether the legal/accounting structure still matches the operational model

## Current recommendation

**Start building the financial architecture now. Start moving real money only when there is a real transaction to support and the ownership/legal structure is settled.**

That avoids premature operational complexity while preventing the first real payment from becoming the event that invents the accounting system.

## Review questions

1. What legal person/entity will ultimately own commercial revenue?
2. What activity, if any, will be community-funded?
3. Will Veiled Dominion have a fiscal host, its own organization, or another structure?
4. Which currencies and countries are expected?
5. Which payment methods will contributors/customers actually need?
6. What information should be public?
7. What information must remain private?
8. What is the minimum chart of accounts needed for the first year?
9. What documentation must accompany each transaction?
10. What should trigger a second-person approval?

**Status remains PROPOSED until these questions are reviewed.**
