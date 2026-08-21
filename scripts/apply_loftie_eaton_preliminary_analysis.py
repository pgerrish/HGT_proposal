from pathlib import Path

tex_path = Path("resistance_networks_full_proposal_v2.tex")
bib_path = Path("resistance_networks_full_proposal_v2.bib")

tex = tex_path.read_text()
bib = bib_path.read_text()

# Add pgfplots only once.
needle = "\\usepackage{graphicx}\n"
if "\\usepackage{pgfplots}" not in tex:
    tex = tex.replace(needle, needle + "\\usepackage{pgfplots}\n\\pgfplotsset{compat=1.18}\n", 1)

section = r'''
\subsection{Preliminary analysis of published longitudinal plasmid data}
\label{sec:prelim_loftie}

Loftie-Eaton et al. experimentally evolved \emph{Pseudomonas} sp. nov. H2 carrying the broad-host-range multidrug-resistance plasmid RP4 and quantified plasmid persistence and cost during host adaptation \citep{loftieeaton2017}. The public data analyzed here comprise 99 replicated 100-generation persistence trajectories sampled at approximately 10-generation intervals across ancestral/evolved host--plasmid combinations, and 36 plasmid-bearing versus plasmid-free competition trajectories. We reconstructed carrier frequency from colony counts and defined
\[
V=\Delta\log\!\left[\frac{p}{1-p}\right],
\]
using a Jeffreys half-count correction when one colony class was absent. For the persistence data we analyzed consecutive 10-generation changes; for the competition data we used one endpoint change per trajectory.

We tested the finite-range form predicted above by fitting the positive-$V$ complementary cumulative distribution after scaling $v=V/\operatorname{median}(V\mid V>0)$. The theory-constrained model was
\begin{equation}
S(v)=A v^{-1}\exp\!\left[-\lambda(v-v_c)_+\right],
\label{eq:prelim_truncated_tail}
\end{equation}
with the power-law exponent fixed at $-1$, normalization $A$ profiled analytically, and two fitted shape parameters: cutoff onset $v_c$ and exponential truncation strength $\lambda$. The fit was restricted to the upper 75\% of positive observations so that the power law is treated as an intermediate-tail hypothesis rather than a model near $V=0$.

In the competition data, 25 of 36 endpoint changes were positive; the fit gave $v_c=1.42$ and $\lambda=1.36$, corresponding to $V_c=1.20$ in unscaled log-odds units (Fig.~\ref{fig:loftie_comp}). In the persistence data, 181 of 990 10-generation changes were positive; the corresponding fit gave $v_c=1.70$ and $\lambda=1.10$, with $V_c=0.98$ (Fig.~\ref{fig:loftie_persist}). In both datasets the empirical CCDF follows the fixed $v^{-1}$ branch over an intermediate range before bending downward. These analyses are preliminary rather than confirmatory: carrier frequencies were estimated from finite colony samples (typically 52 colonies), repeated increments within a persistence trajectory are correlated, and formal comparison with lognormal, Weibull, and free-exponent alternatives remains to be performed. The immediate result is methodological feasibility: an independent published plasmid--host dataset already permits the finite-cutoff analysis proposed for Activity Area~1.

\begin{figure}[H]
\centering
\begin{tikzpicture}
\begin{axis}[
    width=0.70\textwidth,height=5.0cm,
    xmode=log,ymode=log,
    xmin=0.1,xmax=3.0,ymin=0.025,ymax=1.08,
    xlabel={$v/\operatorname{median}(v\mid v>0)$},
    ylabel={$\mathcal{P}(V>v\mid V>0)$},
    grid=both,
    tick label style={font=\scriptsize},
    label style={font=\small},
    legend style={font=\scriptsize,draw=none,at={(0.02,0.03)},anchor=south west},
    clip=false]
\addplot+[only marks,mark=*,mark size=1.35pt] coordinates {
(0.1204,1) (0.18074,0.96) (0.18078,0.92) (0.27026,0.88) (0.37076,0.84) (0.38453,0.8) (0.48689,0.76) (0.52358,0.72) (0.55772,0.68) (0.62924,0.64) (0.79447,0.6) (0.97525,0.56) (1,0.52) (1.0441,0.48) (1.09,0.44) (1.1585,0.4) (1.1878,0.36) (1.2009,0.32) (1.4954,0.28) (1.5292,0.24) (1.5888,0.2) (1.7775,0.16) (1.9679,0.12) (2.0455,0.08) (2.5039,0.04)
};
\addlegendentry{empirical CCDF}
\addplot+[domain=0.486891:2.58,samples=120,dashed,thick] {0.440091/x};
\addlegendentry{untruncated $v^{-1}$}
\addplot+[domain=0.486891:1.416286,samples=50,very thick] {0.440091/x};
\addplot+[domain=1.416286:2.58,samples=90,very thick,forget plot] {0.440091/x*exp(-1.364507*(x-1.416286))};
\addlegendentry{truncated fit}
\addplot+[dotted,thick,forget plot] coordinates {(1.416286,0.025) (1.416286,0.3107)};
\end{axis}
\end{tikzpicture}
\caption{\textbf{Direct competition trajectories.} Empirical CCDF of positive endpoint changes in plasmid-carrier log-odds from the Loftie-Eaton et al. competition experiments, normalized by the positive median (25 positive trajectories of 36) \citep{loftieeaton2017}. The dashed curve is the untruncated $v^{-1}$ continuation. The solid curve is Eq.~\eqref{eq:prelim_truncated_tail} with fitted $v_c=1.42$ and $\lambda=1.36$; the dotted line marks the onset of exponential truncation.}
\label{fig:loftie_comp}
\end{figure}

\begin{figure}[H]
\centering
\begin{tikzpicture}
\begin{axis}[
    width=0.70\textwidth,height=5.0cm,
    xmode=log,ymode=log,
    xmin=0.1,xmax=4.5,ymin=0.004,ymax=1.08,
    xlabel={$v/\operatorname{median}(v\mid v>0)$},
    ylabel={$\mathcal{P}(V>v\mid V>0)$},
    grid=both,
    tick label style={font=\scriptsize},
    label style={font=\small},
    legend style={font=\scriptsize,draw=none,at={(0.02,0.03)},anchor=south west},
    clip=false]
\addplot+[only marks,mark=*,mark size=1.1pt] coordinates {
(0.13177,1) (0.13726,0.99448) (0.14279,0.98895) (0.14642,0.98343) (0.15073,0.9779) (0.16185,0.97238) (0.17743,0.96685) (0.17743,0.96133) (0.18754,0.9558) (0.18754,0.95028) (0.18754,0.94475) (0.19973,0.93923) (0.23309,0.9337) (0.23309,0.92818) (0.23309,0.92265) (0.25647,0.91713) (0.25647,0.9116) (0.25647,0.90608) (0.2662,0.90055) (0.27702,0.89503) (0.28684,0.8895) (0.28684,0.88398) (0.32772,0.87845) (0.32772,0.87293) (0.32772,0.8674) (0.33081,0.86188) (0.34639,0.85635) (0.34639,0.85083) (0.36496,0.8453) (0.36496,0.83978) (0.38544,0.83425) (0.38727,0.82873) (0.39797,0.8232) (0.40145,0.81768) (0.40619,0.81215) (0.41436,0.80663) (0.47283,0.8011) (0.47283,0.79558) (0.47283,0.79006) (0.48956,0.78453) (0.50824,0.77901) (0.50824,0.77348) (0.53393,0.76796) (0.53871,0.76243) (0.54331,0.75691) (0.54331,0.75138) (0.54594,0.74586) (0.57969,0.74033) (0.6019,0.73481) (0.61456,0.72928) (0.6203,0.72376) (0.6203,0.71823) (0.6203,0.71271) (0.6203,0.70718) (0.6203,0.70166) (0.64745,0.69613) (0.64745,0.69061) (0.64745,0.68508) (0.64745,0.67956) (0.64745,0.67403) (0.64745,0.66851) (0.64745,0.66298) (0.64745,0.65746) (0.64745,0.65193) (0.64745,0.64641) (0.64745,0.64088) (0.64745,0.63536) (0.64745,0.62983) (0.64745,0.62431) (0.64745,0.61878) (0.64745,0.61326) (0.64745,0.60773) (0.64745,0.60221) (0.64745,0.59669) (0.64745,0.59116) (0.64745,0.58564) (0.64745,0.58011) (0.64745,0.57459) (0.64745,0.56906) (0.64745,0.56354) (0.64745,0.55801) (0.64745,0.55249) (0.64745,0.54696) (0.64745,0.54144) (0.64745,0.53591) (0.64745,0.53039) (0.64745,0.52486) (0.64745,0.51934) (0.64745,0.51381) (0.64745,0.50829) (0.64745,0.50276) (0.64745,0.49724) (0.64745,0.49171) (0.64745,0.48619) (0.64745,0.48066) (0.64745,0.47514) (0.64745,0.46961) (0.64745,0.46409) (0.64745,0.45856) (0.64745,0.45304) (0.64745,0.44751) (0.64745,0.44199) (0.64745,0.43646) (0.64745,0.43094) (0.64745,0.42541) (0.64745,0.41989) (0.64745,0.41436) (0.64745,0.40884) (0.64745,0.40331) (0.64745,0.39779) (0.64745,0.39227) (0.64745,0.38674) (0.64745,0.38122) (0.64745,0.37569) (0.64745,0.37017) (0.64745,0.36464) (0.64745,0.35912) (0.64745,0.35359) (0.64745,0.34807) (0.64745,0.34254) (0.64745,0.33702) (0.64745,0.33149) (0.64745,0.32597) (0.64745,0.32044) (0.64745,0.31492) (0.64745,0.30939) (0.64745,0.30387) (0.64745,0.29834) (0.64745,0.29282) (0.64745,0.28729) (0.64745,0.28177) (0.64745,0.27624) (0.64745,0.27072) (0.64745,0.26519) (0.64745,0.25967) (0.64745,0.25414) (0.64745,0.24862) (0.64745,0.24309) (0.64745,0.23757) (0.64745,0.23204) (0.64745,0.22652) (0.64745,0.22099) (0.64745,0.21547) (0.64745,0.20994) (0.64745,0.20442) (0.64745,0.1989) (0.64745,0.19337) (0.64745,0.18785) (0.64745,0.18232) (0.64745,0.1768) (0.64745,0.17127) (0.64745,0.16575) (1.9452,0.16022) (1.9452,0.1547) (1.9452,0.14917) (1.9452,0.14365) (1.9452,0.13812) (1.9452,0.1326) (1.9452,0.12707) (1.9452,0.12155) (1.9452,0.11602) (1.9829,0.1105) (2.0667,0.10497) (2.0931,0.099448) (2.3496,0.093923) (2.3496,0.088398) (2.4016,0.082873) (2.4016,0.077348) (2.7973,0.071823) (2.8682,0.066298) (2.8682,0.060773) (2.8682,0.055249) (2.8682,0.049724) (2.8682,0.044199) (3.4885,0.038674) (3.4885,0.033149) (3.4885,0.027624) (3.4885,0.022099) (3.4885,0.016575) (3.4885,0.01105) (3.9613,0.0055249)
};
\addlegendentry{empirical CCDF}
\addplot+[domain=0.543309:4.08,samples=140,dashed,thick] {0.505159/x};
\addlegendentry{untruncated $v^{-1}$}
\addplot+[domain=0.543309:1.701440,samples=60,very thick] {0.505159/x};
\addplot+[domain=1.701440:4.08,samples=100,very thick,forget plot] {0.505159/x*exp(-1.096668*(x-1.701440))};
\addlegendentry{truncated fit}
\addplot+[dotted,thick,forget plot] coordinates {(1.701440,0.004) (1.701440,0.2969)};
\end{axis}
\end{tikzpicture}
\caption{\textbf{Plasmid-persistence trajectories.} Empirical CCDF of positive 10-generation changes in plasmid-carrier log-odds from the Loftie-Eaton et al. persistence experiments, normalized by the positive median (181 positive increments of 990) \citep{loftieeaton2017}. The dashed curve is the untruncated $v^{-1}$ continuation; the solid curve is Eq.~\eqref{eq:prelim_truncated_tail} with fitted $v_c=1.70$ and $\lambda=1.10$. Repeated increments within a trajectory are correlated, so this figure is a descriptive feasibility analysis rather than an independent-event likelihood test.}
\label{fig:loftie_persist}
\end{figure}

'''

anchor = "\\subsection{Plasmid-specific extensions}"
if "\\label{sec:prelim_loftie}" not in tex:
    if anchor not in tex:
        raise SystemExit("Insertion anchor not found")
    tex = tex.replace(anchor, section + anchor, 1)

ref = r'''

@article{loftieeaton2017,
  author  = {Loftie-Eaton, Wesley and Bashford, Kelsie and Quinn, Hannah and Dong, Kieran and Millstein, Jack and Hunter, Samuel and Thomason, Maureen K. and Merrikh, Houra and Ponciano, Jose M. and Top, Eva M.},
  title   = {Compensatory mutations improve general permissiveness to antibiotic resistance plasmids},
  journal = {Nature Ecology \\& Evolution},
  year    = {2017},
  volume  = {1},
  pages   = {1354--1363},
  doi     = {10.1038/s41559-017-0243-2}
}
'''
if "@article{loftieeaton2017," not in bib:
    bib = bib.rstrip() + ref + "\n"

tex_path.write_text(tex)
bib_path.write_text(bib)
