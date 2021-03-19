# Template for using Py2neo 

Recommendation: use a virtual environment to ensure correct Python versions and isolated package installation.

1. Create virtual environment
   
   On windows: `py -m virtualenv venv` (or equivalent)
2. Start virtual environment
   
   On windows: `.\\\\venv\\scripts\\activate.ps1` (I have this aliased in bash as `startvenv`)
3. Install required packages -- one of two ways
   * `pip install py2neo` (if this is the only package)
   * `py -m pip install -r requirements.txt` (or equivalent, if you have `requirements.txt`)
4. Start up local Neo4j database, run file, enter required inputs. 
   
   Should expect all nodes, all properties, and specific properties to be printed.

