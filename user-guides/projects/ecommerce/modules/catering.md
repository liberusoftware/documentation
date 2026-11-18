# Catering: requesting and managing an event

Enter the event date/time and timezone, venue, guest count, dietary requests and service needs. Review the menu quantities before submitting. Dietary requests need operator confirmation; the request alone does not guarantee suitability.

Review the exact quotation revision, currency, expiry and event details before accepting. A changed menu or guest count may need a new quote. Acceptance, availability confirmation, order creation, deposit and payment completion appear separately. If conversion is pending, refresh its status or contact staff with the reference rather than placing the event again.

Authorized staff maintains meals, private recipes/yields and packages, reviews event requirements and confirms availability through the approved workflow. Customers never receive recipe/preparation details or ingredient costs. Staff can investigate and safely resume a failed conversion without changing accepted snapshots.

See the [delivery and ownership guide](../../../../projects/ecommerce/CATERING.md). Screens and integrations remain planned until the relevant host release implements them.

<!-- module-scope:start -->
**Availability:** this is a task/experience contract. Confirm the enabled application and your permitted actions; a documented capability or source package does not prove that every screen is deployed.

## Module-specific scope

The intended **Catering** workspace covers meals, recipes and yields, staff-managed catering packages, event-specific menu revisions, and event/service requirements, enabling reproducible quotations and idempotent order conversion within Ecommerce.

The relevant capability areas are **Meals and ingredient composition**, **Recipes and preparation yields**, **Staff-managed catering packages**, **Event requirements and venue context**, **Immutable menu revisions**, **Reproducible quotation context**, **Availability confirmation and order conversion**. Use their actual enabled screens/operations rather than treating every area as an interchangeable create/edit/delete resource.

## Follow the task safely

1. Open the enabled module from the appropriate project workspace and confirm the current account/team and any relevant entity, store, site or record scope.
2. Review the selected record/context, current state, source evidence and available actions. A visible action can still be restricted by record policy, approval, version or effective date.
3. Enter the required information using the actual form labels and authorized choices. Review any preview/approval summary and submit the explicit action; a generic status edit is not a substitute for a business transition.
4. Read the result. Queued/running means work continues; confirm a final business outcome only when the owner reports it. Keep an operation/reference link for long-running or uncertain work.
5. Correct field errors with the safe draft preserved. Reload/review a changed record before resubmitting; after a timeout, inspect the existing operation/current record before repeating a write.

Different modules have different valid commands, permissions and correction rules. Posted, accepted, published or otherwise finalized records may require a dedicated correction/reversal process rather than ordinary deletion. The owning module contract determines the actual behavior.

## Administrator and developer references

The [source map](../../../../projects/ecommerce/SOURCE-MAPPING.md#catering) distinguishes target requirements, source identities and layer availability. It does not certify runtime parity.

Ecommerce also implements this product scope in application-owned code outside `modules/`. Preserve the module and review its [application capability map](../../../../projects/ecommerce/SOURCE-APPLICATION.md).

Presentation/transport detail: [API plan](../../../../projects/ecommerce/api/catering.md) · [Next.js plan and shared adapter home](../../../../projects/ecommerce/nextjs/catering.md). Inertia and independent API clients can share domain/UI contracts while keeping their navigation, session and form lifecycles separate.
<!-- module-scope:end -->
