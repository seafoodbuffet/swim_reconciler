## Swim Roster Reconciliation
This simple python app parses Team Manager 5.0 rosters in CSV format (run an athlete report, export to CSV)
and a SwimTopia roster file in hy3 format and looks for mismatches. Specifically, it identifies two issues:

* swimmers who are inactive in Team Manager but appear in SwimTopia (ALL swimmers in SwimTopia are presumed active)
* swimmers who are active in Team Manager but do NOT appear in SwimTopia

A sample report output looks like this:

```
Johannes Brahms is active in Team Manager, but NOT in SwimTopia roster
Douglas MacArthur is inactive in Team Manager, but in SwimTopia roster
Marky Marc is active in Team Manager, but NOT in SwimTopia roster
Billy Bob is active in Team Manager, but NOT in SwimTopia roster
```
_names resembling actual persons living or dead is purely coincidence_

To run, execute the following: `python test.py <team manager file> <swimtopia file>`

There's also an optional Docker container in which you can run the program. Simply drop files
name `tm_mgr.csv` and `swimtopia.hy3` into your current directory and run the following commands

```
docker build -t reconcile .
docker run --rm reconcile
```
