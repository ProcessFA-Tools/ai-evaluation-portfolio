# Technical glossary

This glossary defines terms used in the portfolio. Each definition applies to the examples and case studies in this repository.

| Term | Meaning |
| --- | --- |
| AI evaluation | A reviewer checks an AI answer against stated requirements and evidence. |
| Synthetic data | These are invented data used for an example or test. They do not describe a real customer case. |
| Candidate answer | This is one answer that a reviewer scores. The portfolio candidates are authored examples, not recorded AI outputs. |
| Reference answer | This answer shows the expected result under the task's stated assumptions. |
| Reference code | This code calculates an expected result or applies a stated decision rule. |
| Rubric | These scoring rules define how a reviewer awards points for each criterion. |
| Scoring anchor | This description states what an answer must contain to earn a specified score. |
| Criterion | This is one requirement that a reviewer scores. |
| Critical gate | This is a correctness rule that an answer must pass, regardless of its total score. |
| Quality assurance (QA) | These checks help establish whether a process or result meets stated requirements. |
| Validation | These checks establish whether a result or method meets its intended requirements. Evidence applies only to the checked scope. |
| Provenance | This is the record of where a value came from and how the process changed it. |
| Traceability | This lets a reviewer connect a result to its source inputs and processing steps. |
| Source location | This identifies where a value appears in the source, such as a page and row. |
| HMB | A heat and material balance records energy and material flows for a defined system. |
| Phase | This is a distinct physical state, such as gas or liquid. Software can identify multiple liquid phases. |
| In-situ property | This property describes the fluid at its local flowing pressure and temperature. |
| Stock-tank property | This property describes the fluid at specified stock-tank conditions. It is not automatically equal to an in-situ property. |
| Absolute pressure | This pressure uses a perfect vacuum as its zero reference. |
| Gauge pressure | This pressure uses atmospheric pressure as its zero reference. |
| Pressure basis | This label states which reference the pressure uses, such as gauge or absolute. |
| Pa, kPa, bar | These are pressure units. One kPa equals 1,000 Pa. One bar equals 100,000 Pa. |
| Mass balance | This comparison checks incoming and outgoing mass, with accumulation included when applicable. Each exercise states its assumptions. |
| Steady state | The system's state does not change with time. Mass does not accumulate within the defined system. |
| Mass imbalance | In the exercise, this is the outgoing mass flow minus the incoming mass flow. Both flows use the same unit. |
| Tolerance | This is the permitted difference or error under a stated acceptance rule. |
| Null | This marks a value that is absent or unknown. It does not mean zero. |
| Calibration | This process relates source positions or measurements to a specified reference scale. |
| Confidence score | This value indicates the system's confidence. It is not proof of correctness or necessarily a calibrated probability. |
| OCR | Optical character recognition converts an image of text into machine-readable text. |
| Interpolation | This estimates a value between known data points. The estimate is not a direct source measurement. |
| Vector geometry | These shapes use points and lines, rather than an image grid. |
| Raster | This is a grid of cells. Each cell contains a value, such as a traversal cost. |
| NoData | This marks a raster cell without a valid data value. The route example treats such cells as unreachable. |
| Local extrema | These are points where a value is higher or lower than nearby values. |
| Hard constraint | This is a mandatory rule. A lower cost does not permit a route to break it. |
| Soft penalty | This increases a route's cost. Unlike a hard constraint, it does not automatically exclude the route. |
| Feasible route | This route meets all stated mandatory rules. |
| Global optimum | This is the best valid result across the full search space. Comparing a limited candidate list does not prove global optimality. |
| Denominator | This is the number below the division line in a fraction. |
| Relative change | This expresses a difference relative to a stated reference value. The task defines the denominator and sign. |
| P/T | This abbreviation means pressure and temperature. |
| Boundary conditions | These are specified values or rules at the limits of a simulation, such as inlet pressure. |
| Field identifier | This label identifies a data field in a software output. |
| Phase mapping | This rule connects a software phase label to the phase represented in a report. |
| Engine | This program performs the simulation or calculation. |
| Toolkit | This software interface lets another program control the simulation engine. |
| Runtime | This is the software environment used when a program runs. |
| Mocked test | This test substitutes controlled examples for a real dependency, such as a simulation engine. |
| Regression test | This test checks that a change does not break behavior that previously worked. |
| Input hash | This calculated identifier helps detect changes to input data. |
| API key | This credential gives a program access to a service. The public exercises do not require one. |
| Binary | This is a compiled program file. An engine check can require one specific binary. |
| SI | The International System of Units provides standard physical units, including metres, kilograms, seconds, and kelvin. |
| GPL-3.0 | This is the GNU General Public License, version 3. The route case study identifies upstream code with this license. |

PIPESIM, Multiflash, and QGIS are product names. Exact phase labels, such as `LIQUID1`, retain the meaning assigned by the source software.

[Return to the portfolio](../README.md).
