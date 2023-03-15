Can you make this code OOP and professional. I am using functions defined in the previous codes

prof_names = []
postdoc_names = []
phd_names = []

url = 'https://chemie.unibas.ch/en/people/'

table = get_names_from_uni(url)
lastnames = lastname(table)
firstnames = firstname(table)

phd_table = get_phd_names_from_uni(soup)
phd_lastnames  = phd_lastname(phd_table)
phd_firstnames = phd_firstname(phd_table)

for i in range(len(phd_lastnames)):
    rname = " ".join([phd_firstnames[i], phd_lastnames[i]])
    UniBasel_phds.append(rname)
    
UniBasel_phds = [en_decoder(x) for x in UniBasel_phds]

for i in range(len(lastnames)):
    rname = " ".join([firstnames[i], lastnames[i]])
    names.append(rname)
    
 df_prof = pd.DataFrame(columns=(['name','id','cite_total','cite_last5', 'h_total', 'h_last5', 'i_total', 'i_last5']))
df_postdoc = pd.DataFrame(columns=(['name','id','cite_total','cite_last5', 'h_total', 'h_last5', 'i_total', 'i_last5']))
df_phd = pd.DataFrame(columns=(['name','id','cite_total','cite_last5', 'h_total', 'h_last5', 'i_total', 'i_last5']))

postdoc_table = get_postdoc_names_from_uni(soup)
postdoc_lastnames = lastname(postdoc_table)
postdoc_firstnames = firstname(postdoc_table)

for i in range(len(postdoc_lastnames)):
    rname = " ".join([postdoc_firstnames[i], postdoc_lastnames[i]])
    UniBasel_postdocs.append(rname)

UniBasel_postdocs = [en_decoder(x) for x in UniBasel_postdocs]

for i in range(len(UniBasel_postdocs)):
    
    try:
        researcher_name = UniBasel_postdocs[i]
        search_term = UniBasel_postdocs[i] + " university basel google scholar"
        results = scholar_search(search_term)
        researcher_id = results[0].split('=')[1]
        print(researcher_id)
        cite_total, cite_last5, h_total, h_last5, i_total, i_last5 = get_researcher_stats(researcher_id)

        dfr = {'name' : researcher_name, 'id' : researcher_id, 'cite_total' : cite_total,
              'cite_last5' : cite_last5, 'h_total' : h_total, 'h_last5' : h_last5, 
               'i_total' :i_total, 'i_last5' : i_last5}

        df_phd = df_phd.append(dfr,ignore_index=True)
    except:
        pass
      
      
  df_phd['cite_total']= df_phd['cite_total'].astype(str).astype(int)
df_phd['cite_last5']=df_phd['cite_last5'].astype(str).astype(int)
df_phd['h_total']= df_phd['h_total'].astype(str).astype(int)
df_phd['h_last5']=df_phd['h_last5'].astype(str).astype(int)
df_phd['i_total']=df_phd['i_total'].astype(str).astype(int)
df_phd['i_last5']=df_phd['i_last5'].astype(str).astype(int)

