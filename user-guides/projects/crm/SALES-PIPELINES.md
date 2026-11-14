# Work with sales pipelines

A pipeline groups opportunities into stages, helping a sales team track progress toward a sale. This guide describes the workflow reviewed in the CRM source; your organization's screens, labels and available actions may differ. Ask your administrator if sales pipelines are enabled and you need access. The source review did not test every installed interface.

## Prepare a pipeline

Select the appropriate team before working. In the reviewed workflow, the team owner and members with an administrator, manager or sales representative role can make pipeline changes.

1. Create a pipeline and give it a name that identifies the sales process.
2. Add stages in the order your team uses them, such as qualification and proposal. Each stage needs a name and position. Depending on the screen, you may also set a probability and a number of days after which an inactive opportunity is considered stalled.
3. Check that the pipeline and stages appear in the correct team before adding opportunities.

## Track an opportunity

1. Create an opportunity in the appropriate pipeline and stage, and give it a name. Add the value, expected close date or other details where available.
2. Review the opportunity as work progresses. Move an open opportunity to another stage in the same pipeline when it reaches that stage. Check the displayed stage after the move.
3. When the outcome is known, use the available close action to mark it won or lost. The reviewed close workflow requires a reason for a loss. Check the resulting status after submitting.

The reviewed workflow rejects moving a closed opportunity and moving an opportunity to its current stage. It also rejects closing an opportunity that is already closed. A status field on a particular screen may not use the same close workflow; confirm the appropriate procedure with your administrator rather than assuming that editing a status performs every closing step.

## Resolve common problems

- **Pipeline or opportunity not visible:** check your current team, filters and access. The reviewed board shows at most 100 opportunities, so an absent record is not necessarily missing.
- **Move rejected:** check that the opportunity is open and the destination is a different stage in the same pipeline. Refresh the record if someone else may have changed it.
- **Loss cannot be submitted:** enter a loss reason and check that the opportunity is still open.
- **Result uncertain after a timeout:** reopen the opportunity and check its current stage or status before trying again. Contact your administrator if the result remains unclear.

The [sales-pipeline module guide](modules/sales-pipelines.md) describes the broader planned experience. For source details, permissions and known differences between interfaces, see the [technical workflow and source review](../../../projects/crm/guides/SALES-PIPELINES.md).
