# PCR2021

from altair.vegalite.v4.schema.channels import Key
import streamlit as st
import hashlib
import calplot
import pandas as pd
import glob
import plotly.express as px
import os

st.set_page_config(
    page_title='Prod Monitor',
    layout='wide',
    page_icon='bar-chart',
)

# load user authentication
_usps = dict(st.secrets['auth_users'])

def read_table(filename):
        df = pd.read_excel(filename,
                        sheet_name='Prodiarias', 
                        skiprows=9,
                        usecols="A,B,V,AC,AM,AT,AX,BB",
                        nrows=31,
                        names=['DAY','MED','SOS','MSE','JDM','PIN','PAL','EDI']
                    )
        # remove empty rows from botton
        df.dropna(axis=0, how='any', inplace=True)
        return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True, show_spinner=False)
def combine_tables(filelist):
    df = pd.DataFrame(data=None, columns=['DAY','MED','SOS','MSE','JDM','PIN','PAL','EDI'])
    barprog = st.progress(0.0)
    # step = 1/len(filelist)
    niter = 0
    
    for i in filelist:
        fname = i.split('\\')[-1]
        print(f'Loading {niter}/{len(filelist)}')
        st.write('Loading: ', fname)
        niter += 1

        df_temp = read_table(i)
        df = pd.concat([df, df_temp])
        
        barprog.progress(niter/len(filelist))
    return df

def fnum(filepath):
    return int(os.path.basename(filepath).split('_')[0])

# Auth form
with st.sidebar.form(key='user_form'):
    u_name = st.text_input('User', key='user')
    u_pass = st.text_input('Password', type='password', key='password')
    u_submit = st.form_submit_button('Enter')

if u_submit:
    if not u_name:
        st.warning('User Required')
        st.stop()
    
    if not u_pass:
        st.warning('Password required')
        st.stop()

st.title('Production Monitor')

# Password validation
if u_name in _usps:

    if str(hashlib.sha256(u_pass.encode()).hexdigest()) == _usps[u_name]:

        filelist = glob.glob(r'./data/*.xlsx')
        filelist.sort(key=fnum)

        df = combine_tables(filelist)

        # Set Date index 
        df['DATE'] = pd.date_range(start='01/01/2021', periods=len(df), freq='D')
        df.set_index('DATE', inplace=True)

        # calculate totals
        df['TOTAL_ARG'] = df.iloc[:, 1:5].sum(axis=1)
        df['TOTAL'] = df.iloc[:, 1:8].sum(axis=1)
                
        # calplots
        st.header('Daily Calendar Plot')
        selection = ['MED','SOS','MSE','JDM','PIN','PAL','EDI']
        for f in selection:
            figa, ax = calplot.calplot(df[f], cmap='jet', figsize=(15,3), yearlabels=False)
            st.subheader(f)
            st.pyplot(figa)        
        
        # lineplot
        st.header('Daily Production Graph')
        figb = px.line(df, y=selection)
        figb.update_yaxes(title='Production m3/d')
        figb.update_xaxes(title='Date', tickangle=-90)
        figb.update_layout(legend=dict(title='Area'))
        st.plotly_chart(figb)

        # show table
        st.header('Daily Production Table')
        df.index = df.index.strftime('%Y-%m-%d')
        st.dataframe(df.drop(['DAY'], axis=1))

        st.subheader('Statistics')
        st.dataframe(df.describe())

        # filelist.sort(key=fnum, reverse=True)
        # st.write(filelist)
        

    else:
        st.warning('Invalid Password')

else:
    st.info('Log in with a valid user')


