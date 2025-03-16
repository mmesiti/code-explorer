#!/usr/bin/env python3
from sys import argv
import sqlite3
import pandas as pd
import plotly.express as px

def get_path_and_link(origpath,localrepopath,repolink,sep,default_branch="main"): 
    localpath = origpath
    path_from_reporoot = localpath.replace(localrepopath,'')
    path_split = path_from_reporoot.split('/')
    dirname = path_split[:-1]
    basename = path_split[-1]
    path =  repolink.replace('.git','') +f"/blob/{default_branch}/" + path_from_reporoot 

    res = sep.join(dirname) + sep + '<a href="{}" style="color: #000000; text-decoration: underline;">{}</a>'.format(path,basename)
    return res 


def main(cloc_db_filename,
        output_fig_filename,
        repolink=None,
        localrepopath=None,
        default_branch=None):
    connection = sqlite3.connect(cloc_db_filename)
    df = pd.read_sql_query("SELECT * from t;",connection)
    connection.close()

    separator_for_trick = "####"
    paths = (df["File"]
            .apply(lambda p: 
                get_path_and_link(p, localrepopath, repolink, separator_for_trick,default_branch)
                if repolink else p.replace('/',separator_for_trick))
            .str.split(separator_for_trick,expand=True))

    df_expanded = df.merge(paths, 
                           left_index=True,
                           right_index=True)
   

    fig = px.treemap(df_expanded, 
                     path=list(range(0,len(paths.columns))),
                     color="Language",
                     values="nCode")
    
    fig.show()
    print(f"Writing file {output_fig_filename}")
    fig.write_html(output_fig_filename)

cloc_db_filename = argv[1]
output_fig_filename = argv[2]

try:
    repolink=argv[3]
    localrepopath=argv[4]
    default_branch=argv[5]
except:
    repolink=None
    localrepopath=None
    default_branch=None

    pass

main(cloc_db_filename,output_fig_filename,repolink,localrepopath,default_branch)

