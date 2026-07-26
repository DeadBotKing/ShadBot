\# Next Tasks



\## Phase 1 - Snapshot Builder



Status:

NEXT





Create:



infrastructure/snapshot







Implement:



SnapshotBuilder





Responsibilities:



\- Receive ProjectEntity

\- Scan workspace metadata

\- Count files

\- Count directories

\- Generate file hashes

\- Create ProjectSnapshot





\---



\## Phase 2 - Real Language Detector





Implement:



infrastructure/analysis/language\_detector.py







Detect:



\- Python

\- JavaScript

\- TypeScript

\- C#

\- Java

\- C++

\- etc.





Output:



set\[str]





\---



\## Phase 3 - Framework Detector





Detect frameworks:





Examples:



Python:



\- Django

\- FastAPI

\- Flask





JS:



\- React

\- Angular

\- Vue





.NET:



\- ASP.NET





\---



\## Phase 4 - Dependency Analyzer





Analyze:



Python:



\- requirements.txt

\- pyproject.toml





Node:



\- package.json





.NET:



\- csproj





Output:



dict\[str,str]





\---



\## Phase 5 - Git Intelligence





Create:



infrastructure/git







Analyze:



\- repository status

\- branch

\- latest commit

\- changed files





\---



\## Phase 6 - Knowledge Builder





Create:



ProjectKnowledge generation.





Input:



ProjectSnapshot





Output:



ProjectKnowledge





\---



\## Phase 7 - Context Builder





Create AI context layer.





Output:



ProjectContext





Used by:



Agent Platform





\---



\## Phase 8 - Reporting





Generate:



\- Architecture report

\- Dependency report

\- Technology report

\- Project summary

