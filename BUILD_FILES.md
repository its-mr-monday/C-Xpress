# Build Files for C-Xpress

## Build Files are written in json format
Each build file for a project must be specified to the compiler at build time
It specifies all paths for the compiler to consider for files

builder.json sample file:

    {
        "project_name" : "HelloWorld",
        "m_files" : "",
        "mh_files" : "",
        "subdirectories" : {
            "" : ""
        }
    }