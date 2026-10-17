# Validation record

## Check the public exercises

The reference code uses Python 3.10 or newer and the Python standard library. The tests check calculations and decision rules. They include invalid inputs and values at specified limits.

1. Open the repository folder.
2. Run the tests:

```sh
python -m unittest discover -s tests -v
```

3. Check the local documentation links:

```sh
python tools/check_links.py
```

The [Portfolio checks workflow](https://github.com/ProcessFA-Tools/ai-evaluation-portfolio/actions/workflows/verify.yml) runs these checks on Python 3.10 and 3.12. Its status and logs show the current results for the public repository.

## Evidence for the private projects

The case studies describe an inspection of application code and tests. Their file references identify the inspected components. The references do not link to public source files.

Portfolio preparation did not include a new PIPESIM or Multiflash simulation. It did not include a complete QGIS test or a new extraction from a source drawing. The public examples demonstrate specific evaluation methods without those applications.

The PIPESIM case study identifies a difference between the code and the older README. Current code and tests define compatibility more accurately than the older text. A previous live test could not start the simulation server. That failure does not establish whether the unit conversions or report logic are correct.

## What the checks establish

The checks support the synthetic examples and the input requirements covered by the tests. They do not establish these conclusions:

- A numerical model represents a real fluid accurately.
- A selected route meets the requirements of real terrain.
- A recovered drawing value is accurate without a check of the source.

Each conclusion needs its own inputs and validation evidence.

[Read the technical glossary](glossary.md). · [Return to the portfolio](../README.md).
