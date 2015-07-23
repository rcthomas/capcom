# capcom

All communication with astronauts in space passes through a single individual in Mission Control, the Capsule Commander (capcom).

C3 processing applications run in various contexts, and in all those contexts need to know what to do at run-time.
During development, debug, and test they run on laptops or desktops, possibly without internet access.
In production, they run on compute clusters or even supercomputers, at concurrencies that are possibly problematic for out-of-band coordination with e.g. a database-based task server.
The simplest solution is to have a robust method for creating configuration and task data/metadata files that C3 applications know how to consume and interpret.
Making this solution the official way to communicate tasks to C3 applications is what `capcom` does.

For now `capcom` provides access to databases and files on disk, and generates configuration and task files with input from a user.
These configuration and task files are YAML, so they are human readable, human editable, portably parsable, and possibly trackable in revision control.
Further, `capcom` defines and implements the data model for C3 configuration and tasks, in coordination with what works best for C3 applications.
