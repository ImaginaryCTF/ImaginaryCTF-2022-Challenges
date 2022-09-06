# bsv
**Category**: Misc
**Difficulty**: Easy
**Author**: Astro

## Description

I just made my own file format. It's called BSV, for BEE-separated-values! See if you can recover my secret flag.

Note: You will need to add the {} of the flag yourself. Please make the flag all lowercase. Flag format: ictf{[a-zA-Z0-9_]*}

## Distribution

flag.bsv

## Solution

flag.bsv is a csv file with commas replaced with "BEE". Find/replace BEE with "," and then open in Excel. You can resize the columns to see the flag written out.
