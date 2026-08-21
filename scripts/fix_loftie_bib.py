from pathlib import Path
p = Path('resistance_networks_full_proposal_v2.bib')
s = p.read_text()
s = s.replace('Nature Ecology \\\\& Evolution', 'Nature Ecology \\& Evolution')
p.write_text(s)
