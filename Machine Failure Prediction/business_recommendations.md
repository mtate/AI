# Business Recommendations

1. Prioritize inspection when the model flags high risk, especially for readings that push the tree toward the failure branch.
   - Driver: the tree rule based on Rotational speed and Torque.
   - Action: schedule an immediate maintenance check and prepare spare parts.

2. Monitor high tool wear and abnormal temperature combinations closely.
   - Driver: the tree path that splits on Tool wear, Air temperature, and Process temperature.
   - Action: add condition-based monitoring and tighten inspection intervals.

3. Use the model as a recall-focused early warning system rather than a strict pass/fail gate.
   - Driver: the recall-focused framing and the precision guardrail.
   - Action: treat predicted failures as a trigger for proactive intervention, even when the confidence is moderate.

4. For low-risk cases, keep routine maintenance but avoid unnecessary stoppages.
   - Driver: the conservative decision boundary and the precision guardrail.
   - Action: reduce unnecessary downtime by reserving manual inspections for higher-risk cases.
