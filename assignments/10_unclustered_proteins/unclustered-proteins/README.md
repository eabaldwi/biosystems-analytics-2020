# Find unclustered proteins

The file "proteins.fa.cdhit.clstr" contains all of the GI numbers for
proteins that were clustered and put into HMM profiles.  The file
"proteins.fa" contains all proteins (the header is only the GI
number).  Extract the proteins from the "proteins.fa" file that were
not clustered.

Install needed Python modules:

----
$ python3 -m pip install -r requirements
----
