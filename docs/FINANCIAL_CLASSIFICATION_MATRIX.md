# Financial Classification Matrix

**Status:** PROPOSED — WORKING DESIGN  
**Purpose:** Classify money before selecting the transaction/payment path.

| Activity | Economic category | Candidate transaction layer | Candidate payment rail | Administrative evidence | Status |
|---|---|---|---|---|---|
| Community contribution | Community | Open Collective | Open Collective payment processor | iCloud as appropriate | Proposed |
| Sponsorship | Community/project | Open Collective or appropriate entity ledger | PayPal / bank / Wise depending on structure | Agreement + receipt in iCloud | Proposed |
| Grant | Funding | Open Collective or entity ledger | Bank/Wise/other approved rail | Grant agreement + reporting records | Proposed |
| Contributor reimbursement | Expense | Open Collective expense record or entity ledger | Wise / PayPal | Receipt + approval | Proposed |
| Contractor payment | Expense | Entity accounting / project ledger | Wise / PayPal / bank | Contract + invoice + approval | Proposed |
| Commercial sale | Commercial revenue | Commercial accounting ledger | PayPal / bank / other processor | Invoice + order/contract | Proposed |
| Licensing/IP revenue | Commercial/IP | Commercial accounting ledger | Bank / PayPal / other agreed rail | License + invoice + rights records | Proposed |
| Royalty | Commercial/IP | Commercial accounting ledger | Bank / Wise / other agreed rail | Royalty statement + agreement | Proposed |
| Currency conversion | Treasury cost | Accounting/transaction record | Wise or other provider | Provider statement | Proposed |
| Payment-processing fee | Transaction cost | Same ledger as underlying transaction | PayPal/Open Collective/etc. | Processor statement | Proposed |

## Rules

1. **Classify first; route second.**
2. A payment processor is not automatically the accounting system.
3. A transfer between the project's own financial accounts is not new revenue.
4. Processor fees, host fees, bank fees, and currency-conversion costs should be separately identifiable.
5. Community and proprietary/commercial activity should remain distinguishable.
6. Public transaction visibility should never be assumed to mean that contracts, receipts, tax records, payment details, or other private evidence are public.
7. This matrix is a design artifact, not tax or legal advice.

## Minimum transaction fields

Every live transaction should be capable of being reconciled using:

- transaction ID
- date
- gross amount
- currency
- category
- payer/payee
- purpose/project
- payment rail
- processor/host fees
- net amount
- destination/source account
- supporting document reference
- approval status
- reconciliation status
- public/private classification

## First implementation target

Before opening multiple live financial channels, build a **dry-run ledger** containing fictional transactions covering:

- one contribution
- one sponsorship
- one grant
- one reimbursement
- one contractor invoice
- one commercial sale
- one licensing payment
- one currency conversion
- one refund/chargeback scenario

The goal is to prove the classification and reconciliation model before real money is involved.
