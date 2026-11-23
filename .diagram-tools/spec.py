"""Framing text for this framework's diagrams.

Phase content comes from the reference design; only the framing below is
authored, and each line is drawn from that document's stated scope.
"""

FRAMING = {'kicker': 'HIPAA Security Rule',
 'title_tail': '&mdash; HIPAA',
 'sub': 'From agent coverage to continuous proof between audits &mdash; exports map '
        'to control IDs in the Reporting &amp; Evidence section.',
 'caution_label': 'Scope &rsaquo;',
 'caution': 'CSW evidences the <b>technical safeguards</b> around systems that '
            'process ePHI. Workforce training, business associate agreements, risk '
            'analysis documentation and physical safeguards are separate programmes.',
 'takeaway': 'CSW turns observed traffic into designed isolation and keeps producing '
             'evidence after the project ends. <b>The quarterly binder is the '
             'deliverable</b> &mdash; it is what an auditor consumes without a live '
             'walkthrough.',
 'rail': ['Machine-generated flow evidence, not hand-drawn diagrams',
          'Simulation proves the policy before anything is enforced',
          'Quarterly packs carry the evidence between audits']}
