# find_files module

more granular variant of the "find_file.py" module that is functional.
will begin including a database that will allow exclusions of files as
well as some other finer control of the file movement and selection.

goal is to build a more robust API that can be integrated with a wider array of 
applications than the current module.

# updates:

# import_manager.py
  though similar to the import_manager found directly in common - it behaves differently: intended for
  use as an imported module, this becomes severely object-oriented.
  * import "import_management"
  access the following:
  * import_management.prune_files_by_name();
  * import_management.add_file();
  * import_management.compare_file();
  


# FUNCTION CALLS:

