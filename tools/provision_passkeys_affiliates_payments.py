#!/usr/bin/env python3
"""Provision and enrich Passkeys, Affiliate Management & Referral Contracts, and Unified Contract-Based Merchant Payment modules across all projects and presentation layers."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PROJECT_META = {
    'boilerplate': {
        'label': 'Boilerplate',
        'scope_doc': 'BOILERPLATE.md',
        'user_guide_title': 'Liberu Laravel Boilerplate',
    },
    'billing': {
        'label': 'Billing',
        'scope_doc': 'BILLING.md',
        'user_guide_title': 'Billing',
    },
    'crm': {
        'label': 'CRM',
        'scope_doc': 'CRM.md',
        'user_guide_title': 'CRM',
    },
    'ecommerce': {
        'label': 'Ecommerce',
        'scope_doc': 'ECOMMERCE.md',
        'user_guide_title': 'Ecommerce',
    },
    'accounting': {
        'label': 'Accounting',
        'scope_doc': 'ACCOUNTING.md',
        'user_guide_title': 'Accounting',
    },
}

NEW_MODULES = [
    # 1. Passkeys & WebAuthn (single shared foundation module in Boilerplate)
    {
        'projects': ['boilerplate'],
        'stem': 'passkeys',
        'title': 'Passkeys and WebAuthn',
        'group': 'Identity and authentication modules',
        'arch_doc': 'PASSKEYS.md',
        'composer_identity': 'liberusoftware/passkeys',
        'extends_contract': 'PasskeyCeremonyServiceContract, PasskeyRegistrarContract, PasskeyAssertionVerifierContract, PasskeyCredentialRepositoryContract, StepUpAuthenticationContract',
        'purpose': (
            'WebAuthn / FIDO2 Relying Party registration and assertion ceremonies, discoverable credentials '
            '(resident keys), passwordless sign-in, cryptographic step-up authentication, attestation and '
            'signature-counter clone detection, authenticator naming and revocation, backup/sync metadata, '
            'and safe fallback recovery policy.'
        ),
        'features': [
            ('WebAuthn registration ceremonies', 'Generate single-use 32-byte challenges and PublicKeyCredentialCreationOptions bound to actor, session, Relying Party ID, and allowed origin.'),
            ('Discoverable credentials and passwordless sign-in', 'Support resident keys and conditional UI autofill mediation for phishing-resistant passwordless authentication without account enumeration.'),
            ('Cryptographic step-up authentication', 'Verify recent user-verified passkey assertions via StepUpAuthenticationContract before payout approvals, refund overrides, token creation, or security changes.'),
            ('Attestation and signature-counter clone detection', 'Validate RP ID hash, origin, COSE public key, user presence/verification flags, and monotonic signature counters, quarantining suspected cloned authenticators.'),
            ('Passkey lifecycle, naming, and revocation', 'List enrolled authenticators with transport/backup flags, last-used metadata, friendly naming, and recent-auth-guarded revocation with lockout prevention.'),
            ('Account recovery and security audit evidence', 'Coordinate fallback policy with Identity Core and Two-Factor Authentication while emitting immutable audit logs and security notifications.'),
        ],
    },
    # 2. Affiliate Contracts (single shared contract module in Boilerplate)
    {
        'projects': ['boilerplate'],
        'stem': 'affiliate-contracts',
        'title': 'Affiliate Contracts',
        'group': 'Affiliate management and referral contracts',
        'arch_doc': 'AFFILIATES.md',
        'composer_identity': 'liberusoftware/affiliate-contracts',
        'extends_contract': 'AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract',
        'purpose': (
            'product-neutral PHP interfaces, immutable attribution and conversion DTOs, commission calculator '
            'contracts, clawback/hold lifecycle states, fraud and self-referral policy contracts, and payout '
            'settlement boundaries that any repository (CRM, Billing, Ecommerce, Accounting) can implement or extend.'
        ),
        'features': [
            ('AffiliateProgramContract and attribution window DTOs', 'Define program terms, attribution windows, first/last/coupon-override models, hold periods, and recurring commission caps without product schema coupling.'),
            ('ReferralAttributionContract and signed touch tokens', 'Standardize referral link/code issuance, first-party click/touch recording, and winning advocate resolution for orders, invoices, subscriptions, or deals.'),
            ('ConversionRecorderContract and idempotent clawbacks', 'Provide product-neutral commands to record qualified conversions and process partial/full clawbacks when orders or invoices are refunded, voided, or disputed.'),
            ('CommissionCalculatorContract and tiered rate rules', 'Define flat, percentage, tiered-volume, product-category, and recurring-installment commission calculation contracts using exact minor-unit money DTOs.'),
            ('FraudAndSelfReferralPolicyContract', 'Define self-referral, shared payment fingerprint, velocity anomaly, and duplicate prospect checks executed before conversion qualification.'),
            ('PayoutSettlementContract and RewardFulfillmentContract', 'Define matured commission locking, minimum payout thresholds, tax/compliance holds, settlement batch handoff to Payment Core/Accounting, and two-sided referral rewards.'),
        ],
    },
    # 3. Affiliates Core Capability (single shared module in Boilerplate)
    {
        'projects': ['boilerplate'],
        'stem': 'affiliates',
        'title': 'Affiliates and Partner Programs',
        'group': 'Affiliate management and referral capabilities',
        'arch_doc': 'AFFILIATES.md',
        'composer_identity': 'liberusoftware/affiliate-core',
        'extends_contract': 'liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)',
        'purpose': (
            'reusable affiliate program administration, partner enrollment and approval, referral links and promotional '
            'codes, first-party click and conversion attribution, tiered and recurring commission ledger, refund/dispute '
            'clawback hold windows, fraud prevention, partner portal read models, and payout settlement batching extending '
            'liberusoftware/affiliate-contracts.'
        ),
        'features': [
            ('Affiliate program and commission tier rules', 'Configure attribution windows, hold periods, flat/percentage/tiered/recurring commission schedules, and product eligibility extending AffiliateProgramContract.'),
            ('Partner applications, KYC/tax readiness, and approval', 'Manage partner enrollment applications, review workflows, tier assignment, and custom partner rate overrides via AffiliatePartnerEnrollmentContract.'),
            ('Tracking links, campaign parameters, and promo codes', 'Issue signed referral links, vanity codes, and campaign creative assets with first-party consent-aware click tracking.'),
            ('Authoritative conversion ingestion and hold ledger', 'Record idempotent conversions from orders, subscriptions, and invoices via ConversionRecorderContract with immutable pending/held/matured ledger states.'),
            ('Automated refund, cancellation, and dispute clawbacks', 'Reverse or adjust pending and matured commissions automatically when upstream payments are refunded, voided, or charged back.'),
            ('Self-referral, velocity, and fraud screening', 'Enforce FraudAndSelfReferralPolicyContract across account, email domain, IP/device velocity, and payment-fingerprint signals with operator review queues.'),
            ('Payout approval batches and settlement handoff', 'Group matured commissions above payout thresholds, enforce tax/compliance holds, and export or disburse via PayoutSettlementContract.'),
        ],
    },
    # 4. Billing Referrals (CRM and Ecommerce already have referrals.md)
    {
        'projects': ['billing'],
        'stem': 'referrals',
        'title': 'Referrals and Advocate Rewards',
        'group': 'Affiliate management and referral capabilities',
        'arch_doc': 'AFFILIATES.md',
        'composer_identity': 'liberusoftware/billing-referrals',
        'extends_contract': 'liberusoftware/affiliate-contracts (ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)',
        'purpose': (
            'customer-to-customer referral programs, advocate share links and codes, referred account/subscription '
            'qualification, two-sided rewards (invoice credits, free months, account balance credits), duplicate and '
            'self-referral fraud controls, and attribution extending liberusoftware/affiliate-contracts.'
        ),
        'features': [
            ('Referral programs and two-sided reward rules', 'Configure advocate and friend incentives (invoice credits, discount coupons, usage credits, or free billing cycles) extending AffiliateProgramContract.'),
            ('Advocate share links and referral codes', 'Generate unique customer referral links and codes inside the customer portal via ReferralAttributionContract.'),
            ('Referred signup and subscription qualification', 'Track referred accounts from signup through paid invoice/subscription maturity before unlocking rewards via ConversionRecorderContract.'),
            ('Duplicate, household, and self-referral prevention', 'Enforce FraudAndSelfReferralPolicyContract against shared payment methods, billing addresses, and account self-dealing.'),
            ('Automated reward fulfillment and clawback handling', 'Apply earned credits or discounts via RewardFulfillmentContract and reverse unapplied rewards on early cancellation or chargeback.'),
        ],
    },
    # 5. Payment Contracts (single shared contract module in Boilerplate)
    {
        'projects': ['boilerplate'],
        'stem': 'payment-contracts',
        'title': 'Payment Contracts',
        'group': 'Unified merchant payment architecture',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-contracts',
        'extends_contract': 'PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract',
        'purpose': (
            'provider-neutral merchant payment gateway interfaces, immutable money and payment-intent DTOs, '
            'canonical 3DS/SCA and capture/refund/dispute lifecycle state machine, saved payment method and mandate '
            'vault contracts, cryptographic webhook verification contracts, and settlement reconciliation interfaces '
            'extended by all merchant payment adapters (Stripe, PayPal, Paddle, Adyen, Mollie, Square, GoCardless).'
        ),
        'features': [
            ('PaymentGatewayAdapterContract and capability descriptors', 'Declare provider identity, supported currencies, payment method families, capture/refund modes, and credential health checks via PaymentCapabilityDescriptorDto.'),
            ('PaymentIntentServiceContract and 3DS/SCA client actions', 'Standardize create/confirm/cancel payment intents and normalized client actions (redirect URL, 3DS2 challenge, SDK client token, or terminal handoff).'),
            ('PaymentCaptureAndRefundContract with idempotency', 'Define full/partial capture, authorization void, and full/partial refund commands using exact minor-unit amounts and deterministic idempotency keys.'),
            ('SavedPaymentMethodVaultContract and mandates', 'Define PCI-safe tokenized payment method setup, recurring card/wallet vaulting, and Direct Debit mandate lifecycle contracts.'),
            ('MerchantWebhookVerifierContract', 'Standardize raw-payload signature/HMAC verification, replay-window enforcement, and normalization into MerchantWebhookEventDto.'),
            ('DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract', 'Define chargeback evidence submission, dispute state transitions, and gross-to-net fee/payout settlement batch reconciliation.'),
        ],
    },
    # 6. Payment Core (single shared orchestration module in Boilerplate)
    {
        'projects': ['boilerplate'],
        'stem': 'payment-core',
        'title': 'Payment Core',
        'group': 'Unified merchant payment architecture',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-core',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayRegistryContract, PaymentOrchestratorContract, WebhookInboxProcessorContract, SettlementReconciliationEngineContract)',
        'purpose': (
            'provider-neutral merchant payment orchestration, gateway adapter registry and routing, immutable '
            'transaction and attempt ledger, deterministic idempotency locking, verified webhook inbox/outbox '
            'deduplication, vaulted payment method and mandate lifecycle, dispute tracking, and gross-to-net '
            'settlement reconciliation consuming liberusoftware/payment-contracts.'
        ),
        'features': [
            ('Payment gateway registry and tenant/currency routing', 'Register merchant adapters implementing PaymentGatewayAdapterContract and route checkout/invoice intents by tenant, currency, tender type, and failover policy.'),
            ('Payment intent orchestration and state machine', 'Coordinate authorization, 3DS/redirect continuation, capture, void, and failure recovery across any installed gateway adapter.'),
            ('Idempotency locking and immutable transaction ledger', 'Prevent duplicate charges or refunds across concurrent retries and record every gateway attempt, provider reference, and money movement.'),
            ('Tokenized payment method vault and mandate directory', 'Manage customer cards, wallets, and bank mandates through SavedPaymentMethodVaultContract without storing raw cardholder data.'),
            ('Verified webhook inbox and out-of-order reconciliation', 'Verify signatures via MerchantWebhookVerifierContract, deduplicate by provider event ID, and apply monotonic state transitions safely.'),
            ('Dispute management and settlement batch reconciliation', 'Track chargeback deadlines/evidence and reconcile provider payout batches, merchant fees, and FX differences against local ledgers.'),
        ],
    },
    # 7. Payment Stripe (single shared Stripe adapter module in Boilerplate)
    {
        'projects': ['boilerplate'],
        'stem': 'payment-stripe',
        'title': 'Payment Stripe Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-stripe',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)',
        'purpose': (
            'the single shared Stripe merchant payment provider adapter built on the latest stripe/stripe-php SDK '
            '(^20.3+) and pinned StripeClient API version, extending liberusoftware/payment-contracts and consolidating '
            'liberusoftware/billing-stripe for PaymentIntents, SetupIntents, CustomerSession, Checkout\\Session, '
            'ConfirmationToken, Stripe Payment Element, Apple Pay / Google Pay / Link / SEPA / ACH / Klarna, manual '
            'and automatic capture, full/partial refunds, Radar disputes, Stripe Terminal POS readers, '
            'BalanceTransaction settlement reconciliation, and Webhook::constructEvent signature verification.'
        ),
        'features': [
            ('Latest Stripe SDK client and pinned API version', 'Instantiate \\Stripe\\StripeClient (stripe/stripe-php ^20.3+) per tenant credential with explicit pinned stripe_version, max_network_retries, and per-request idempotency_key options.'),
            ('PaymentIntents, Checkout Sessions, and 3DS2/SCA confirmation', 'Implement PaymentIntentServiceContract using automatic_payment_methods, ConfirmationToken, CustomerSession, and next_action 3DS/redirect handling.'),
            ('SetupIntents and PaymentMethod vaulting', 'Implement SavedPaymentMethodVaultContract for off-session recurring cards, wallets, SEPA Direct Debit, and US Bank Account mandates.'),
            ('Full/partial capture, cancellation, and idempotent refunds', 'Implement PaymentCaptureAndRefundContract with deterministic Stripe idempotency_key options and provider reference tracking.'),
            ('Stripe-Signature webhook verification and normalization', 'Implement MerchantWebhookVerifierContract using \\Stripe\\Webhook::constructEvent() with timestamp tolerance and raw-body verification into MerchantWebhookEventDto.'),
            ('Stripe disputes, Terminal POS, and BalanceTransaction reconciliation', 'Implement DisputeAndChargebackHandlerContract, POSHardwareTerminalContract, and PayoutAndSettlementReconcilerContract for disputes, Terminal readers, and payout fee/FX reconciliation.'),
        ],
    },
    # 8. Payment PayPal
    {
        'projects': ['boilerplate'],
        'stem': 'payment-paypal',
        'title': 'Payment PayPal Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-paypal',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)',
        'purpose': (
            'PayPal Complete Payments and Braintree merchant provider adapter extending liberusoftware/payment-contracts '
            'for PayPal Orders v2, PayPal Wallet, Pay Later, Venmo, Vault v3 setup/payment tokens, authorization and '
            'capture, full/partial refunds, Customer Disputes API, Payouts/settlement reporting, and cryptographic '
            'webhook transmission signature verification.'
        ),
        'features': [
            ('PayPal Orders v2 creation, approval, and authorization', 'Implement PaymentIntentServiceContract for PayPal Wallet, Pay Later, and card orders with payer-action approval redirects and JS SDK order IDs.'),
            ('PayPal Vault v3 setup tokens and recurring payment tokens', 'Implement SavedPaymentMethodVaultContract for vaulted PayPal accounts and cards with merchant-initiated billing agreements.'),
            ('Order capture, authorization reauthorization/void, and refunds', 'Implement PaymentCaptureAndRefundContract for v2/payments/authorizations/{id}/capture, void, and captures/{id}/refund with PayPal-Request-Id idempotency.'),
            ('PayPal transmission-signature webhook verification', 'Implement MerchantWebhookVerifierContract verifying PAYPAL-TRANSMISSION-SIG, transmission time, cert URL, and CRC32/signature validation.'),
            ('PayPal Customer Disputes and chargeback lifecycle', 'Implement DisputeAndChargebackHandlerContract for CUSTOMER.DISPUTE.* events, evidence documents, and outcome reconciliation.'),
            ('PayPal transaction search and settlement reconciliation', 'Implement PayoutAndSettlementReconcilerContract mapping gross amounts, PayPal fee breakdowns, currency conversions, and settlement batches.'),
        ],
    },
    # 9. Payment Paddle
    {
        'projects': ['boilerplate'],
        'stem': 'payment-paddle',
        'title': 'Payment Paddle Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-paddle',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)',
        'purpose': (
            'Paddle Billing Merchant-of-Record provider adapter extending liberusoftware/payment-contracts and '
            'bridging liberusoftware/billing-paddle for global tax-inclusive/exclusive transactions, Paddle.js '
            'overlay/inline checkout, saved payment methods, subscription billing bridge, credit/refund adjustments, '
            'chargeback write-offs, payout fee/tax reconciliation, and Paddle-Signature webhook verification.'
        ),
        'features': [
            ('Paddle Billing transactions and Merchant-of-Record checkout', 'Implement PaymentIntentServiceContract for Paddle transactions, localized tax calculation, and Paddle.js client transaction tokens.'),
            ('Paddle adjustments for full/partial refunds and credits', 'Implement PaymentCaptureAndRefundContract mapping Paddle transaction capture and refund/credit adjustment workflows.'),
            ('Customer saved payment methods and subscription bridge', 'Implement SavedPaymentMethodVaultContract for Paddle customer payment methods and recurring subscription renewal synchronization.'),
            ('Paddle-Signature ts/h1 HMAC webhook verification', 'Implement MerchantWebhookVerifierContract validating Paddle-Signature timestamp and HMAC-SHA256 digest over raw request bytes.'),
            ('Tax, Merchant-of-Record fee, and payout reconciliation', 'Implement PayoutAndSettlementReconcilerContract capturing Paddle MoR tax remittance, processing fees, chargebacks, and payout remittances.'),
        ],
    },
    # 10. Payment Adyen
    {
        'projects': ['boilerplate'],
        'stem': 'payment-adyen',
        'title': 'Payment Adyen Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-adyen',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)',
        'purpose': (
            'Adyen global acquiring and omnichannel provider adapter extending liberusoftware/payment-contracts '
            'for Adyen Checkout sessions/payments, Web/Mobile Drop-in and Components, 3DS2 native/redirect challenges, '
            'stored payment methods, asynchronous capture/cancel/refund modifications, POS Terminal API, chargeback '
            'defense, settlement detail reports, and HMAC-SHA256 webhook notification verification.'
        ),
        'features': [
            ('Adyen Checkout sessions, /payments, and 3DS2 action handling', 'Implement PaymentIntentServiceContract for Adyen sessions, /payments, and /payments/details with normalized redirect, threeDS2, and voucher actions.'),
            ('Asynchronous capture, technical cancel, and refund modifications', 'Implement PaymentCaptureAndRefundContract over /payments/{paymentPspReference}/captures, /cancels, and /refunds correlated by PSP reference.'),
            ('Tokenization and recurring storedPaymentMethod vaulting', 'Implement SavedPaymentMethodVaultContract for shopperReference recurring tokens (cardOnFile, subscription, unscheduledCardOnFile).'),
            ('Adyen HMAC-SHA256 webhook notification verification', 'Implement MerchantWebhookVerifierContract verifying merchantHMAC signatures across AUTHORISATION, CAPTURE, REFUND, CANCEL_OR_REFUND, and CHARGEBACK events.'),
            ('Omnichannel POS Terminal API and settlement batch reconciliation', 'Implement POSHardwareTerminalContract for Cloud/Local Terminal API payment requests and PayoutAndSettlementReconcilerContract for settlement batch reports.'),
        ],
    },
    # 11. Payment Mollie
    {
        'projects': ['boilerplate'],
        'stem': 'payment-mollie',
        'title': 'Payment Mollie Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-mollie',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)',
        'purpose': (
            'Mollie European and multi-method payment provider adapter extending liberusoftware/payment-contracts '
            'for iDEAL, Bancontact, SEPA Direct Debit, cards, Apple Pay, Klarna, Mollie Components, customer mandates, '
            'manual/automatic capture, full/partial refunds, chargebacks, settlements API reconciliation, and webhook verification.'
        ),
        'features': [
            ('Mollie Payments API, Components, and APM redirects', 'Implement PaymentIntentServiceContract for iDEAL, Bancontact, cards, Klarna, and SEPA with checkout redirect URLs and embedded card token support.'),
            ('Mollie Customers and SEPA/card recurring Mandates', 'Implement SavedPaymentMethodVaultContract for first-payment mandate creation, mandate validation, and off-session recurring charges.'),
            ('Authorized payment capture, release, and partial refunds', 'Implement PaymentCaptureAndRefundContract for manual-capture payment methods and queued/immediate partial refunds.'),
            ('Mollie webhook verification and authoritative state fetch', 'Implement MerchantWebhookVerifierContract combining signed webhook verification and authoritative payment/order status retrieval.'),
            ('Chargeback handling and Settlements API reconciliation', 'Implement DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract for Mollie settlement periods, fees, and chargeback deductions.'),
        ],
    },
    # 12. Payment Square
    {
        'projects': ['boilerplate'],
        'stem': 'payment-square',
        'title': 'Payment Square Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-square',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)',
        'purpose': (
            'Square commerce and POS payment provider adapter extending liberusoftware/payment-contracts for '
            'Square Web Payments SDK, In-App Payments, Cards on File, Cash App Pay, Afterpay, delayed-capture '
            'authorizations, refunds, Square Terminal hardware checkouts, disputes API, payout entries reconciliation, '
            'and x-square-hmacsha256-signature webhook verification.'
        ),
        'features': [
            ('Square Payments API and Web Payments SDK tokenization', 'Implement PaymentIntentServiceContract for tokenized card/wallet/Cash App Pay nonces, buyer verification (3DS/SCA), and location-scoped payments.'),
            ('Delayed capture, CompletePayment, CancelPayment, and Refunds', 'Implement PaymentCaptureAndRefundContract with Square idempotency_key enforcement for partial/full captures, voids, and PaymentRefunds.'),
            ('Square Cards on File and customer vaulting', 'Implement SavedPaymentMethodVaultContract for storing, disabling, and charging customer Cards on File across web, mobile, and POS.'),
            ('Square Terminal API and in-person POS hardware bridge', 'Implement POSHardwareTerminalContract for TerminalCheckout creation, device pairing status, and card-present receipt correlation.'),
            ('HMAC-SHA256 webhook verification, Disputes API, and Payouts', 'Implement MerchantWebhookVerifierContract (`x-square-hmacsha256-signature`), DisputeAndChargebackHandlerContract, and PayoutAndSettlementReconcilerContract.'),
        ],
    },
    # 13. Payment GoCardless
    {
        'projects': ['boilerplate'],
        'stem': 'payment-gocardless',
        'title': 'Payment GoCardless Adapter',
        'group': 'Unified merchant payment adapters',
        'arch_doc': 'PAYMENTS.md',
        'composer_identity': 'liberusoftware/payment-gocardless',
        'extends_contract': 'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)',
        'purpose': (
            'GoCardless bank-to-bank Direct Debit and Open Banking (Instant Bank Pay) provider adapter extending '
            'liberusoftware/payment-contracts for Billing Requests, Bacs/SEPA/ACH/PAD/BECS/Autogiro mandates, '
            'recurring and one-off bank collections, instalment schedules, refunds, chargeback/late-failure handling, '
            'payout reconciliation, and Webhook-Signature HMAC-SHA256 verification.'
        ),
        'features': [
            ('GoCardless Billing Requests and Instant Bank Pay (Open Banking)', 'Implement PaymentIntentServiceContract and SavedPaymentMethodVaultContract for combined mandate + instant open-banking payment authorization flows.'),
            ('Direct Debit Mandate lifecycle (Bacs, SEPA, ACH, PAD, BECS)', 'Manage mandate submission, active/failed/cancelled transitions, customer bank-account tokens, and scheme compliance notices.'),
            ('Bank payment collection, cancellation, retry, and refunds', 'Implement PaymentCaptureAndRefundContract for mandate-backed payment creation, pre-submission cancellation, and approved GoCardless refunds.'),
            ('GoCardless Webhook-Signature HMAC-SHA256 verification', 'Implement MerchantWebhookVerifierContract validating Webhook-Signature digests across mandates, payments, billing_requests, refunds, and payouts events.'),
            ('Late failure, chargeback claim, and payout batch reconciliation', 'Implement DisputeAndChargebackHandlerContract for Direct Debit indemnity claims and PayoutAndSettlementReconcilerContract for payout items and transaction fees.'),
        ],
    },
]


def slugify(label: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')


def render_feature_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    feat_bullets = '\n'.join(
        f'- **{label}:** {desc}' for label, desc in mod['features']
    )
    verify_bullets = '\n'.join(
        f'- Verify {label.lower()} across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.'
        for label, _ in mod['features']
    )
    return f"""# {meta['label']}: {title}

## Canonical independent module specification

**Domain module:** `{dom}`
**Intended package identity:** `{mod['composer_identity']}`
**Extends / implements contracts:** `{mod['extends_contract']}`
**Application:** {meta['label']}  
**Capability group:** {mod['group']}  
**Source scope:** [{meta['scope_doc']}](../{meta['scope_doc']}) · {arch_link}  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · {arch_link} · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The {title} module owns {mod['purpose']} It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

{feat_bullets}

## 3. Ownership and contract boundaries

- **Contract alignment:** Implements and/or exposes `{mod['extends_contract']}` as defined in {arch_link}. Consuming repositories depend on the contract boundary rather than coupling to internal models or vendor SDKs.
- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, Inertia, Next.js, Nuxt, Mobile, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 4. Implementation strategy

### Domain model

- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification and {arch_link}.
- Make invalid states unrepresentable where practical and enforce remaining invariants at every mutation boundary.
- Use opaque stable identifiers and explicit actor, tenant, locale, timezone, and currency context where relevant.

### Application layer

- Implement one application action per mutation/use case and purpose-built queries for reads.
- Authorize before accessing or mutating protected data; navigation or UI visibility never substitutes for a policy.
- Execute local invariant changes transactionally, dispatch events after commit, and make retryable commands idempotent.
- Model long-running or cross-module work through queued jobs, outbox/inbox delivery, sagas, compensation, and operator-visible recovery.

### Persistence and integrations

- Store only module-owned data in module-owned tables with documented indexes, constraints, retention, export, deletion, and migration behavior.
- Integrate other capabilities through contracts/events and external systems through independent provider adapters with timeouts, retries, rate limits, reconciliation, and sandbox support.
- Treat imports, webhooks, provider callbacks, files, and generated content as untrusted inputs with provenance and deduplication.

### Presentation

- Provide matching optional presentation packages only when required: `{dom}-filament`, `{dom}-livewire`, `{dom}-api`, `{dom}-react-inertia`, `{dom}-vue-inertia`, `{dom}-nuxt`, `{dom}-nextjs`, `{dom}-react-native`, and `{dom}-flutter`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

{verify_bullets}
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts (`{mod['extends_contract']}`) and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.
"""


def render_core_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    cap_summary = ', '.join(lbl for lbl, _ in mod['features']) + '.'
    return f"""# {meta['label']}: {title} Core Module

## Package contract

**Design package identifier:** `{dom}`
**Intended Composer identity:** `{mod['composer_identity']}`
**Contracts implemented / exposed:** `{mod['extends_contract']}`
**Domain specification:** [{title}](../features/{stem}.md) · {arch_link}
**Foundation / product specification:** [{meta['scope_doc']}](../{meta['scope_doc']})
**Capability:** {cap_summary}
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of {title}. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability as specified in {arch_link}.

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Implement and bind the public contract interfaces (`{mod['extends_contract']}`) so consuming modules and presentation adapters never couple to concrete storage models or external vendor SDKs.
- Expose typed actions for mutations and purpose-built queries for reads. Keep Eloquent models as persistence mappings and never expose private tables to other modules.
- Enforce authorization, tenant/team context, ownership, consent, and field sensitivity consistently across HTTP, UI, console, queue, export, search, notification, and bulk paths.
- Own migrations, constraints, indexes, factories, seeders, retention, export, deletion, configuration, events, jobs, and safe enable/disable/upgrade behavior.
- Make asynchronous work idempotent, retryable, observable, and safe to replay; dispatch local events after commit and document compensation for distributed work.

## Verification and consumer contract

Test domain rules, contract compliance, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, and representative host composition. Add architecture tests for presentation coupling, provider leakage, private cross-module access, and dependency cycles.

API, Filament, Livewire, React, Vue, Next.js, Nuxt, React Native, and Flutter/Dart consumers use only this package's public contracts. See {arch_link}, [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md).
"""


def render_api_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    bullets = '\n'.join(f'- {lbl}' for lbl, _ in mod['features'])
    return f"""# {meta['label']}: {title} API

## Canonical one-to-one API module specification

**Proposed API design identifier:** `{dom}-api`<br>
**Matching domain module:** `{stem}`  
**Matching core package:** [`{dom}`](../core/{stem}.md) (`{mod['composer_identity']}`)  
**Contracts presented:** `{mod['extends_contract']}`  
**Application:** {meta['label']}  
**Source feature:** [{title}](../features/{stem}.md) · {arch_link}  
**Architecture:** [API.md](../../../architecture/API.md) · {arch_link} · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the {title} domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies (`{mod['extends_contract']}`), and contains no other module's API logic.

The domain capability includes:

{bullets}

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract (`/api/v1/{stem}`).
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit minor-unit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

<!-- observed-api-contract:start -->
## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. See the [API architecture](../../../architecture/API.md), {arch_link}, and [source mapping](../SOURCE-MAPPING.md#{stem}).
<!-- observed-api-contract:end -->

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

## 6. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Add one-to-one architecture tests proving this package depends on and presents only `{stem}`.
"""


def render_filament_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    surf = '\n'.join(
        f"- **{lbl}:** resource/table/form/action or page behavior for this module's authorized workflow."
        for lbl, _ in mod['features']
    )
    caps = '\n'.join(
        f'- `{slugify(lbl)}`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.'
        for lbl, _ in mod['features']
    )
    return f"""# {meta['label']}: {title} Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `{dom}-filament`  
**Matching domain module:** `{stem}`  
**Matching core package:** [`{dom}`](../core/{stem}.md) (`{mod['composer_identity']}`)  
**Application:** {meta['label']}  
**Source feature:** [{title}](../features/{stem}.md) · {arch_link}  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · {arch_link} · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `{stem}` public contract boundary (`{mod['extends_contract']}`). It must not contain another module's UI or depend on application `App\\` classes.

## 2. Module-specific surfaces

{surf}

## 3. Filament 5 implementation

- Register a stable `{dom}-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

{caps}

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.
"""


def render_livewire_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    surf = '\n'.join(
        f'- **{lbl}:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.'
        for lbl, _ in mod['features']
    )
    caps = '\n'.join(
        f'- `{slugify(lbl)}`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.'
        for lbl, _ in mod['features']
    )
    return f"""# {meta['label']}: {title} Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `{dom}-livewire`  
**Matching domain module:** `{stem}`  
**Matching core package:** [`{dom}`](../core/{stem}.md) (`{mod['composer_identity']}`)  
**Application:** {meta['label']}  
**Source feature:** [{title}](../features/{stem}.md) · {arch_link}  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · {arch_link} · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions (`{mod['extends_contract']}`) and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity.

## 2. Module-specific interactions

{surf}

## 3. Livewire 4 implementation

- Register a stable `{dom}-livewire` component namespace and service provider according to [LIVEWIRE.md](../../../standards/LIVEWIRE.md).
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use `#[Locked]` and typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

{caps}

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
"""


def render_inertia_doc(project: str, mod: dict, fw: str) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    fw_label = 'React' if fw == 'react' else 'Vue'
    fw_ver = 'React 19.2' if fw == 'react' else 'Vue 3'
    std_doc = 'REACT.md' if fw == 'react' else 'VUE.md'
    hook_dir = 'hooks' if fw == 'react' else 'composables'
    surf = '\n'.join(
        f"- **{lbl}:** page, component, hook, form, and failure-state behavior for this module's authorized workflow."
        for lbl, _ in mod['features']
    )
    caps = '\n'.join(
        f'- `{slugify(lbl)}`: map the matching API query/action to a focused {fw_label} page, component, hook, or Inertia form.'
        for lbl, _ in mod['features']
    )
    return f"""# {meta['label']}: {title} {fw_label} + Inertia

## Canonical one-to-one {fw_label}/Inertia implementation

**Package:** `{dom}-{fw}-inertia`
**Matching domain module:** `{stem}`
**Matching core package:** [`{dom}`](../core/{stem}.md) (`{mod['composer_identity']}`)
**Application:** {meta['label']}
**Source feature:** [{title}](../features/{stem}.md) · {arch_link}
**Architecture:** [{std_doc}](../../../standards/{std_doc}) · {arch_link} · [API.md](../../../architecture/API.md) · [Matching API module](../api/{stem}.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional {fw_ver} + Inertia 3 presentation package adapts the matching domain contract (`{mod['extends_contract']}`) through Laravel-owned Inertia routes. It contributes reusable Inertia pages, {fw_label} components, {hook_dir}, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary.

## 2. Module-specific surfaces

{surf}

## 3. {fw_ver} + Inertia 3 implementation

- Register a stable `{dom}-{fw}-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, {hook_dir} under `resources/js/{hook_dir}`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

{caps}

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
"""


def render_nuxt_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    surf = '\n'.join(
        f"- **{lbl}:** page/component/composable/API-action behavior for this module's authorized workflow."
        for lbl, _ in mod['features']
    )
    caps = '\n'.join(
        f'- `{slugify(lbl)}`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.'
        for lbl, _ in mod['features']
    )
    return f"""# {meta['label']}: {title} Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `{dom}-nuxt`
**Matching domain module:** `{stem}`
**Matching core package:** [`{dom}`](../core/{stem}.md) (`{mod['composer_identity']}`)
**Application:** {meta['label']}
**Source feature:** [{title}](../features/{stem}.md) · {arch_link}
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · {arch_link} · [API.md](../../../architecture/API.md) · [Matching API module](../api/{stem}.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module (`{mod['extends_contract']}`). It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `{stem}` public API boundary.

## 2. Module-specific surfaces

{surf}

## 3. Nuxt 4 implementation

- Register a stable `{dom}-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

{caps}

## 4. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
"""


def render_mobile_doc(project: str, mod: dict, layer: str) -> str:
    stem = mod['stem']
    title = mod['title']
    dom = f'module-{project}-{stem}' if project != 'boilerplate' else f'module-{stem}'
    arch_link = f'[{mod["arch_doc"]}](../../../architecture/{mod["arch_doc"]})'
    if layer == 'react-native':
        surf_name = 'React Native + Expo'
        std_link = '[React Native + Expo standard](../../../standards/REACT-NATIVE.md)'
        tech_link = '[React Native + Expo technology](../../../technologies/REACT-NATIVE.md)'
        bullet1 = '- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.'
    else:
        surf_name = 'Flutter + Dart'
        std_link = '[Flutter + Dart standard](../../../standards/FLUTTER.md)'
        tech_link = '[Flutter + Dart technology](../../../technologies/FLUTTER.md)'
        bullet1 = '- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.'
    return f"""# {title} {surf_name}

**Package:** `{dom}-{layer}`
**Matching domain module:** `{stem}`
**Matching core package:** `{dom}` ([implementation](../core/{stem}.md))
**Matching API package:** `{dom}-api` ([contract](../api/{stem}.md))
**Architecture specification:** {arch_link}

## Implementation plan

This adapter presents {title} (`{mod['extends_contract']}`) for the {surf_name} surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

{bullet1}
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test {title} API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See {std_link}, {arch_link}, [mobile architecture](../../../architecture/MOBILE.md), {tech_link}, [core module](../core/{stem}.md), and [API module](../api/{stem}.md).
"""


def render_user_guide_doc(project: str, mod: dict) -> str:
    meta = PROJECT_META[project]
    stem = mod['stem']
    title = mod['title']
    ref_line = (
        f'**Core module:** [{stem}.md](../../../../projects/{project}/core/{stem}.md)'
        if project == 'boilerplate'
        else f'**Feature specification:** [{stem}.md](../../../../projects/{project}/features/{stem}.md)'
    )
    return f"""# {meta['label']} {title} — end-user guide

**Project:** [{meta['user_guide_title']}](../README.md)
{ref_line}
**Architecture reference:** [{mod['arch_doc']}](../../../../architecture/{mod['arch_doc']})
**Shared experience standard:** [Web and mobile](../../../WEB-AND-MOBILE.md)

## What users see

See the {title} context first, then the next safe action. The module should explain its purpose in the page heading, keep related evidence close to the decision, and never require users to understand internal package names.

## Primary journey

```mermaid
flowchart LR
  A[Open module] --> B[Understand context]
  B --> C[Take primary action]
  C --> D[See result or queued status]
  D --> E[Continue or recover]
```

## Web behavior

Use a responsive page with a clear title, status/freshness, primary action, related context, and helpful empty/error states. Deep links should reopen the same safe context. Forms preserve entered data after validation errors; destructive or externally visible actions explain their impact before confirmation.

## Mobile behavior

Prioritize the frequent task and essential context. Keep the primary action reachable, use readable cards instead of dense tables, expose sync freshness, preserve drafts, and handle offline, interrupted, denied, and conflict states without claiming success prematurely. Notifications and deep links must respect permission and privacy.

## Visible states

- **Empty:** explain what is missing and the next useful setup or discovery step.
- **Success:** confirm what changed, when, and what the user can do next.
- **Queued:** show that processing continues, who owns it, and where progress appears.
- **Failure/conflict:** explain the problem in plain language and provide retry, review, or support recovery.
- **Denied:** explain the safe reason and an appropriate request/access path.

## Developer expectation

An installed surface is ready when this journey is represented in the relevant web/mobile navigation, authorization is enforced by the server, API errors map to accessible UI, loading and interruption are tested, and the module's terminology is consistent across web, mobile, email, and notifications.
"""


def update_existing_module_specs():
    """Update existing Stripe, Paddle, Payments, Affiliate, and Referral feature specs so they explicitly extend payment-contracts / affiliate-contracts."""
    updates = [
        # Billing existing Stripe & Paddle & Payments
        (
            'billing',
            'module-billing-stripe',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)',
            [
                ('Consolidate into shared liberusoftware/payment-stripe', 'Bridge existing billing-stripe driver registrations into the single shared liberusoftware/payment-stripe adapter using stripe/stripe-php ^20.3+ and pinned StripeClient API version.'),
                ('PaymentIntent and SetupIntent orchestration', 'Implement PaymentIntentServiceContract and SavedPaymentMethodVaultContract for Stripe PaymentIntents, SetupIntents, CustomerSession, 3DS2/SCA client actions, and off-session payment methods.'),
                ('Payment capture and idempotent refunds', 'Implement PaymentCaptureAndRefundContract for full/partial capture, authorization void, and full/partial refunds with deterministic Stripe idempotency_key options.'),
                ('Stripe-Signature webhook verification and normalization', 'Implement MerchantWebhookVerifierContract via \\Stripe\\Webhook::constructEvent() to verify raw webhook signatures and emit normalized MerchantWebhookEventDto events into payment-core.'),
                ('Dispute defense and settlement reconciliation', 'Implement DisputeAndChargebackHandlerContract and PayoutAndSettlementReconcilerContract for Stripe Radar disputes and BalanceTransaction payout reconciliation.'),
                ('Provider references and gateway driver bridge', 'Maintain backward-compatible GatewayDriver registration with module-billing-payments while conforming to the canonical payment-stripe adapter contract.'),
            ],
        ),
        (
            'billing',
            'module-billing-paddle',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)',
            [
                ('Paddle Billing transactions and Merchant-of-Record checkout', 'Implement PaymentIntentServiceContract for Paddle Billing transactions, localized tax calculation, and Paddle.js client checkout tokens.'),
                ('Transaction capture and full/partial refund adjustments', 'Implement PaymentCaptureAndRefundContract for Paddle transaction capture and credit/refund adjustment lifecycles.'),
                ('Saved payment methods and subscription renewal bridge', 'Implement SavedPaymentMethodVaultContract for vaulted customer payment methods and recurring subscription billing synchronization.'),
                ('Paddle-Signature webhook verification and normalization', 'Implement MerchantWebhookVerifierContract validating timestamped HMAC-SHA256 Paddle-Signature headers into normalized MerchantWebhookEventDto records.'),
                ('Provider references, MoR tax/fee breakdown, and settlement reconciliation', 'Implement PayoutAndSettlementReconcilerContract and maintain backward-compatible GatewayDriver registration with module-billing-payments.'),
            ],
        ),
        (
            'billing',
            'payments',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts, liberusoftware/payment-core',
            [
                ('Unified payment-contracts and payment-core integration', 'Delegate gateway driver resolution to liberusoftware/payment-core and provider adapters (payment-stripe, payment-paypal, payment-paddle, payment-adyen, payment-mollie, payment-square, payment-gocardless) implementing liberusoftware/payment-contracts.'),
                ('Methods and vaulted payment instruments', 'Manage customer cards, wallets, and payment tokens through SavedPaymentMethodVaultContract without storing raw cardholder data.'),
                ('Mandates and Direct Debit lifecycles', 'Manage SEPA, Bacs, ACH, and recurring billing mandates across GoCardless, Stripe, Mollie, and Adyen adapters.'),
                ('Gateway drivers and capability discovery', 'Bridge GatewayManager with PaymentGatewayAdapterContract capability descriptors, credential health checks, and tenant/currency routing.'),
                ('Capture, partial invoice payments, and allocation', 'Execute authorized captures via PaymentCaptureAndRefundContract and allocate funds across invoices and account balances.'),
                ('Refunds and credit reversals', 'Execute full and partial refunds with deterministic idempotency keys and approval policies.'),
                ('Disputes and chargeback evidence', 'Track provider disputes via DisputeAndChargebackHandlerContract, evidence deadlines, and win/loss accounting adjustments.'),
                ('Reconciliation and settlement batches', 'Reconcile local payment records against provider balance transactions, fees, and payout batches via PayoutAndSettlementReconcilerContract.'),
            ],
        ),
        (
            'billing',
            'module-billing-payments',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts, liberusoftware/payment-core',
            [
                ('Unified payment-contracts and payment-core integration', 'Delegate gateway driver resolution to liberusoftware/payment-core and provider adapters (payment-stripe, payment-paypal, payment-paddle, payment-adyen, payment-mollie, payment-square, payment-gocardless) implementing liberusoftware/payment-contracts.'),
                ('Methods and vaulted payment instruments', 'Manage customer cards, wallets, and payment tokens through SavedPaymentMethodVaultContract.'),
                ('Mandates and Direct Debit lifecycles', 'Manage SEPA, Bacs, ACH, and recurring billing mandates across installed merchant adapters.'),
                ('Gateway drivers and capability discovery', 'Bridge GatewayDriver and GatewayManager with PaymentGatewayAdapterContract.'),
                ('Capture and allocation', 'Execute idempotent payment captures and allocate receipts to open invoices.'),
                ('Refunds and disputes', 'Process full/partial refunds and manage chargeback disputes through unified contracts.'),
                ('Reconciliation', 'Match local payments against merchant settlement batches and provider references.'),
            ],
        ),
        # Ecommerce existing Payments & Payment Operations & Referrals & Commissions
        (
            'ecommerce',
            'payments',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts, liberusoftware/payment-core',
            [
                ('Shared payment-contracts and payment-core integration', 'Consume liberusoftware/payment-contracts and liberusoftware/payment-core so Stripe, PayPal, Paddle, Adyen, Mollie, Square, and GoCardless adapters plug in without checkout schema changes.'),
                ('Tender selection and dynamic capability routing', 'Present eligible payment methods (cards, Apple/Google Pay, PayPal, BNPL, iDEAL, SEPA, POS terminal) using PaymentCapabilityDescriptorDto.'),
                ('Authorize/capture/void/refund references', 'Execute idempotent PaymentIntentServiceContract and PaymentCaptureAndRefundContract commands correlated to order and fulfillment milestones.'),
                ('Saved payment method vault and 3DS/SCA continuation', 'Support vaulted customer payment instruments and normalized 3DS2/redirect client actions via SavedPaymentMethodVaultContract.'),
                ('Payment status projection and settlement reconciliation', 'Project canonical PaymentLifecycleState onto orders and reconcile gross-to-net merchant settlements via PayoutAndSettlementReconcilerContract.'),
            ],
        ),
        (
            'ecommerce',
            'payment-operations',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts, liberusoftware/payment-core',
            [
                ('Capture/refund queues over payment-contracts', 'Process queued fulfillment-triggered captures and return-triggered refunds through PaymentCaptureAndRefundContract with idempotency locks.'),
                ('Disputes/chargebacks via DisputeAndChargebackHandlerContract', 'Ingest normalized dispute notifications, assemble order/delivery evidence, and track win/loss outcomes across Stripe, PayPal, Adyen, Mollie, Square, and GoCardless.'),
                ('Manual review and fraud-hold release', 'Coordinate manual fraud review holds before capturing or voiding authorized payment intents.'),
                ('Verified provider webhooks via MerchantWebhookVerifierContract', 'Verify cryptographic webhook signatures, deduplicate provider event IDs in the payment-core inbox, and reconcile out-of-order events.'),
                ('Settlement reconciliation via PayoutAndSettlementReconcilerContract', 'Match merchant payout batches, processing fees, FX conversions, and reserve holds against order payment ledgers.'),
                ('Exception handling and operator replay', 'Surface stuck authorizations, failed captures, and mismatched settlements with audited operator retry actions.'),
            ],
        ),
        (
            'ecommerce',
            'referrals',
            'AFFILIATES.md',
            'liberusoftware/affiliate-contracts (AffiliateProgramContract, ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)',
            [
                ('Advocate links/codes via ReferralAttributionContract', 'Issue signed customer referral links, vanity codes, and share tokens extending liberusoftware/affiliate-contracts.'),
                ('Referred customers and checkout attribution', 'Bind first-party referral touches and promo codes to guest and registered checkouts without leaking advocate personal data.'),
                ('Order qualification via ConversionRecorderContract', 'Record qualified referral conversions when referred orders are captured and fulfilled above program thresholds.'),
                ('Two-sided rewards via RewardFulfillmentContract', 'Issue advocate and friend store credit, discount vouchers, or loyalty points upon conversion maturity.'),
                ('Duplicate/fraud rules via FraudAndSelfReferralPolicyContract', 'Block self-referrals, shared payment fingerprints, same-household abuse, and return-gaming with automated clawbacks on order refund.'),
                ('Attribution and status tracking', 'Expose referral conversion status (pending, held, qualified, rewarded, clawed_back) across storefront, API, and admin surfaces.'),
            ],
        ),
        # CRM existing Affiliate Management & Referrals
        (
            'crm',
            'affiliate-management',
            'AFFILIATES.md',
            'liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, FraudAndSelfReferralPolicyContract, PayoutSettlementContract)',
            [
                ('Affiliates and partner profiles', 'Manage affiliate partners, tiers, tax/KYC readiness, and custom commission agreements extending liberusoftware/affiliate-contracts.'),
                ('Applications and onboarding approval', 'Review, approve, or decline affiliate applications via AffiliatePartnerEnrollmentContract.'),
                ('Links, promo codes, and campaigns', 'Issue signed tracking links, campaign parameters, and creative assets via ReferralAttributionContract.'),
                ('Clicks and first-party touch attribution', 'Record consent-aware click touches and resolve first-touch, last-touch, or coupon attribution across leads, deals, orders, and subscriptions.'),
                ('Conversions and cross-product clawback ledger', 'Ingest qualified conversions and refund/chargeback reversals from Billing and Ecommerce via ConversionRecorderContract.'),
                ('Commission rules and tiered calculation', 'Calculate flat, percentage, tiered, and recurring commissions via CommissionCalculatorContract.'),
                ('Payout approvals/exports via PayoutSettlementContract', 'Approve matured commissions after the hold window and export or settle payout batches via Payment Core or Accounting.'),
                ('Disputes, fraud controls, assets, and partner portal', 'Enforce FraudAndSelfReferralPolicyContract, resolve commission disputes, distribute marketing assets, and expose partner portal read models.'),
            ],
        ),
        (
            'crm',
            'crm-affiliate-management',
            'AFFILIATES.md',
            'liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, FraudAndSelfReferralPolicyContract, PayoutSettlementContract)',
            [
                ('Affiliates and partner profiles', 'Manage affiliate partners, tiers, and agreements extending liberusoftware/affiliate-contracts.'),
                ('Applications and onboarding approval', 'Review and approve partner applications via AffiliatePartnerEnrollmentContract.'),
                ('Links, campaigns, and clicks', 'Issue signed referral links and track consent-aware attribution touches via ReferralAttributionContract.'),
                ('Conversions and commission rules', 'Record conversions and calculate tiered/recurring commissions via ConversionRecorderContract and CommissionCalculatorContract.'),
                ('Payout approvals/exports, disputes, assets, and portal', 'Settle matured commissions via PayoutSettlementContract, enforce FraudAndSelfReferralPolicyContract, and serve the affiliate portal.'),
            ],
        ),
        (
            'crm',
            'referrals',
            'AFFILIATES.md',
            'liberusoftware/affiliate-contracts (AffiliateProgramContract, ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)',
            [
                ('Referral programs extending AffiliateProgramContract', 'Define advocate referral programs, eligibility rules, attribution windows, and reward structures via liberusoftware/affiliate-contracts.'),
                ('Links/codes via ReferralAttributionContract', 'Generate trackable referral links, QR codes, and shareable promo codes for advocates.'),
                ('Advocates and referred prospects', 'Link advocate contacts to referred leads, opportunities, and customers with full timeline lineage.'),
                ('Qualification via ConversionRecorderContract', 'Qualify referrals when prospects reach target deal stages, paid invoices, or completed orders.'),
                ('Rewards via RewardFulfillmentContract', 'Fulfill advocate and prospect rewards (credits, gift cards, discounts, or commission payouts) after hold windows mature.'),
                ('Fraud/duplicate controls via FraudAndSelfReferralPolicyContract', 'Prevent self-referrals, duplicate lead gaming, and disallowed domain/payment collisions.'),
                ('Status and multi-touch attribution', 'Track referral lifecycle status and reconcile attribution with CRM Campaigns and Billing/Ecommerce revenue.'),
            ],
        ),
        (
            'crm',
            'crm-referrals',
            'AFFILIATES.md',
            'liberusoftware/affiliate-contracts (AffiliateProgramContract, ReferralAttributionContract, ConversionRecorderContract, FraudAndSelfReferralPolicyContract, RewardFulfillmentContract)',
            [
                ('Referral programs and links/codes', 'Configure referral programs and issue advocate links/codes via liberusoftware/affiliate-contracts.'),
                ('Advocates, prospects, and qualification', 'Track referred prospects and qualify conversions via ReferralAttributionContract and ConversionRecorderContract.'),
                ('Rewards, fraud/duplicate controls, status, and attribution', 'Fulfill rewards via RewardFulfillmentContract and enforce FraudAndSelfReferralPolicyContract.'),
            ],
        ),
        # Accounting Customer Payments & Payment Reconciliation
        (
            'accounting',
            'customer-payments',
            'PAYMENTS.md',
            'liberusoftware/payment-contracts, liberusoftware/payment-core',
            [
                ('Receipts and online payment links via payment-contracts', 'Collect online invoice payments through liberusoftware/payment-core and merchant adapters (Stripe, PayPal, Paddle, Adyen, Mollie, Square, GoCardless) implementing liberusoftware/payment-contracts.'),
                ('Gateway/bank references and provider provenance', 'Store immutable provider transaction references, payment method metadata, and idempotency keys.'),
                ('Deposits and undeposited funds clearing', 'Group merchant receipts into undeposited funds and clearing accounts prior to bank settlement.'),
                ('Allocations and partial/overpayments', 'Allocate receipts across open customer invoices, credit notes, and unapplied cash balances.'),
                ('Refunds and chargeback adjustments', 'Initiate or record gateway refunds and dispute adjustments via PaymentCaptureAndRefundContract and DisputeAndChargebackHandlerContract.'),
                ('Reconciliation with merchant settlements', 'Match customer payment receipts against PayoutAndSettlementReconcilerContract payout batches and bank feeds.'),
            ],
        ),
    ]

    updated_count = 0
    for project, stem, arch_doc, contracts, features in updates:
        feat_path = ROOT / 'projects' / project / 'features' / f'{stem}.md'
        if not feat_path.exists():
            continue
        text = feat_path.read_text()
        arch_link = f'[{arch_doc}](../../../architecture/{arch_doc})'
        if f'({arch_link})' not in text and arch_doc not in text:
            text = re.sub(
                r'(\*\*Architecture:\*\* [^\n]+)',
                lambda m: m.group(1) + f' · {arch_link}',
                text,
                count=1,
            )
        if '**Extends / implements contracts:**' not in text:
            text = re.sub(
                r'(\*\*Domain module:\*\* `[^`]+`\n)',
                lambda m: m.group(1) + f'**Extends / implements contracts:** `{contracts}`\n',
                text,
                count=1,
            )
        bullet_block = '\n'.join(f'- **{lbl}:** {desc}' for lbl, desc in features)
        text = re.sub(
            r'(## 2\. Full feature scope\n\n)(?:- \*\*[^\n]+\n)+',
            lambda m: m.group(1) + bullet_block + '\n',
            text,
            count=1,
        )
        feat_path.write_text(text)
        updated_count += 1
    return updated_count


def remove_duplicate_product_copies():
    """Ensure shared payment, affiliate-contracts/core, and passkeys modules live once in boilerplate rather than duplicated per product."""
    duplicates = [
        ('billing', ['passkeys', 'affiliate-contracts', 'affiliates', 'payment-contracts', 'payment-core', 'payment-stripe', 'payment-paypal', 'payment-paddle', 'payment-adyen', 'payment-mollie', 'payment-square', 'payment-gocardless']),
        ('crm', ['passkeys', 'affiliate-contracts']),
    ]
    removed = 0
    layers = ('features', 'core', 'api', 'filament', 'livewire', 'react', 'vue', 'nuxt', 'nextjs', 'react-native', 'flutter')
    for project, stems in duplicates:
        for stem in stems:
            for layer in layers:
                p = ROOT / 'projects' / project / layer / f'{stem}.md'
                if p.exists():
                    p.unlink()
                    removed += 1
            ug = ROOT / 'user-guides' / 'projects' / project / 'modules' / f'{stem}.md'
            if ug.exists():
                ug.unlink()
                removed += 1
    return removed


def main():
    removed = remove_duplicate_product_copies()
    created_files = 0
    for mod in NEW_MODULES:
        stem = mod['stem']
        for project in mod['projects']:
            p_dir = ROOT / 'projects' / project
            # 1. features
            (p_dir / 'features' / f'{stem}.md').write_text(render_feature_doc(project, mod))
            # 2. core
            (p_dir / 'core' / f'{stem}.md').write_text(render_core_doc(project, mod))
            # 3. api
            (p_dir / 'api' / f'{stem}.md').write_text(render_api_doc(project, mod))
            # 4. filament
            (p_dir / 'filament' / f'{stem}.md').write_text(render_filament_doc(project, mod))
            # 5. livewire
            (p_dir / 'livewire' / f'{stem}.md').write_text(render_livewire_doc(project, mod))
            # 6. react
            (p_dir / 'react' / f'{stem}.md').write_text(render_inertia_doc(project, mod, 'react'))
            # 7. vue
            (p_dir / 'vue' / f'{stem}.md').write_text(render_inertia_doc(project, mod, 'vue'))
            # 8. nuxt
            (p_dir / 'nuxt' / f'{stem}.md').write_text(render_nuxt_doc(project, mod))
            # 9. react-native
            (p_dir / 'react-native' / f'{stem}.md').write_text(render_mobile_doc(project, mod, 'react-native'))
            # 10. flutter
            (p_dir / 'flutter' / f'{stem}.md').write_text(render_mobile_doc(project, mod, 'flutter'))
            # 11. user-guides
            ug_path = ROOT / 'user-guides' / 'projects' / project / 'modules' / f'{stem}.md'
            ug_path.parent.mkdir(parents=True, exist_ok=True)
            ug_path.write_text(render_user_guide_doc(project, mod))
            created_files += 11

    updated_existing = update_existing_module_specs()
    print(f'Removed {removed} duplicate per-product files; provisioned {created_files} shared module files and updated {updated_existing} existing module specifications.')


if __name__ == '__main__':
    main()
