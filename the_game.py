import random

import streamlit as st
from streamlit.elements.widgets import button

st.markdown(
    """
    <style>
    .stApp{
    background-color:#008080;
    font-family:'MS Sans Serif',Arial,sans-serif;
        }
    div.stButton > button , [data-testid = "stButton"] button{
     background-color:#c0c0c0 !important;
     background-image:none !important;
     color: #000000 !important;
     border: 2px solid !important;
     border-color: #ffffff #808080 #808080 #ffffff !important;
     box-shadow: inset 1px 1px #dfdfdf , inset -1px -1px #0a0a0a !important;
     border-radius: 0px !important;
     font-weight:bold !important;
    }
    div.stButton > button:active, [data-testid="stButton"] button:active,
    div.stButton > button:focus, [data-testid="stButton"] button:focus {
    border-color: #808080 #ffffff #ffffff #808080 !important;
    box-shadow: inset 1px 1px #0a0a0a , inset -1px -1px #dfdfdf !important:
    background-color:#b0b0b0 !important;
    background-image: none !important;
    color: #000000 !important;
    }
     
    </style>
    """,
    unsafe_allow_html=True,
)
if "cpu_temp" not in st.session_state:
    st.session_state.cpu_temp = 40
    st.session_state.ram_utilization = 20
    st.session_state.bloatware_list = ["cortona","master chief" ,"ai ","3 mil chrome tabs " , "FH3"]
    st.session_state.active_bloatware_list = []
    st.session_state.apps_running = 0
    st.session_state.crash_coins = 15
    st.session_state.Nitrogen_cooling = False
    st.session_state.thermal_paste_apply = False
    st.session_state.dual_fans_apply = False


if st.session_state.cpu_temp>=100:
        st.markdown("a problem has been dected by windows and caused it to shutdown"
                    "to prevent damage")
        st.error("sys:errr win code : X0700211 (MACHINE-CODE-EXCEPTTTTTIIONNNNNN)")
        st.error("cause:cpu melted,power supply fail,ram fail"
                    "blaotware has destryed your pc plz check before you download something on the internet")
        if st.button("replace pc parts except hhd,cost:15c", key= "hard_reset_temp1"):
            if st.session_state.crash_coins >= 15:
                st.session_state.crash_coins -= 15
                st.session_state.cpu_temp = 55
                st.session_state.ram_utilization = 45
                st.session_state.active_bloatware_list = []
                st.rerun()
            else:
                st.error("you don't hae enough crash coins,the hard reset is the best option")
        if st.button("hard reset , lose save data",key="hard_reset_temp2"):
            st.session_state.cpu_temp = 40
            st.session_state.ram_utilization = 20
            st.session_state.crash_coins = 15
            st.session_state.bloatware_list = ["cortona", "master chief", "ai ", "3 mil chrome tabs ", "FH3"]
            st.session_state.active_bloatware_list = []
            st.session_state.apps_running = 0
            st.session_state.Nitrogen_cooling = False
            st.session_state.thermal_paste_apply = False
            st.session_state.dual_fans_apply = False
            st.rerun()
elif st.session_state.ram_utilization>= 100:
    st.markdown("a problem has been dected by windows and caused it to shutdown"
                "to prevent damage")
    st.error("sys:errr win code : X0700322 (MACHINE-CODE-EXCEPTTTTTIIONNNNNN)")
    st.error("cause:cpu melted,power supply fail,ram fail"
             "blaotware has destryed your pc plz check before you download something on the internet")
    if st.button("replace pc parts except hhd,cost:15c", key="hard_reset_ram1"):
        if st.session_state.crash_coins >= 15:
            st.session_state.crash_coins -= 15
            st.session_state.cpu_temp = 55
            st.session_state.ram_utilization = 45
            st.session_state.active_bloatware_list = []
            st.rerun()
        else:
            st.error("you don't hae enough crash coins,the hard reset is the best option")
    if st.button("hard reset , lose save data", key="hard_reset_ram2"):
        st.session_state.cpu_temp = 40
        st.session_state.ram_utilization = 20
        st.session_state.crash_coins = 25
        st.session_state.bloatware_list = ["cortona", "master chief", "ai ", "3 mil chrome tabs ", "FH3"]
        st.session_state.active_bloatware_list = []
        st.session_state.apps_running = 0
        st.session_state.Nitrogen_cooling = False
        st.session_state.thermal_paste_apply = False
        st.session_state.dual_fans_apply = False
        st.rerun()
else:
    def spawn():
        st.session_state.apps_running += 1
        st.session_state.cpu_temp += random.randint(4,8)
        st.session_state.ram_utilization +=random.randint(3,8)
        if st.session_state.get("thermal_paste_apply",False):
            st.session_state.cpu_temp-=2
        if st.session_state.get("dual_fans_apply",False):
            st.session_state.cpu_temp-=2
            st.session_state.ram_utilization-=2
        app={"name":random.choice(st.session_state.bloatware_list),
             "id":st.session_state.apps_running,
             }

        st.session_state.active_bloatware_list.append(app)
        st.session_state.crash_coins += int(1+ len(st.session_state.active_bloatware_list)*bonus_coin_add)

    with st.sidebar:
        st.subheader("STATS")
        st.subheader(f"💥🪙crash coin balance : {st.session_state.crash_coins} ")
        st.subheader(F"deleated bloatware : {st.session_state.apps_running}")
        st.subheader("⌨️ THE SHOP",help="hover over the upgrades to find out what do they do ")
        if not st.session_state.get("thermal_paste_apply",False):
            if st.button("buy the thermal paste for 55c ❓",help="reduces 2'c form cpu temp when every app runs"):
                if st.session_state.crash_coins >= 55:
                    st.session_state.crash_coins -= 55
                    st.success("the thermal paste has been applied")
                    st.session_state.thermal_paste_apply = True
                    st.rerun()
                else:
                    st.warning("you do not have enough crash coins")
        else:
            st.success("☑️the thermal paste has been applied")
        if not st.session_state.get("dual_fans_apply", False):
            if st.button("buy the dual for 80c ❓",help ="reduces cpu temp and ram uti passively"):
                if st.session_state.crash_coins >= 80:
                    st.session_state.crash_coins -= 80
                    st.success("the dual fans has been applied")
                    st.session_state.dual_fans_apply = True
                    st.rerun()
                else:
                    st.warning("you do not have enough crash coins")
        else:
            st.success("☑️the dual fans has been applied")
        if not st.session_state.get("Nitrogen_cooling", False):
            if st.button("buy the nitrogen cooling [one time use] for 200c ❓",help = "it instantly reduces your cpu temp and ram utilization . A lifesaver you know "):
                if st.session_state.crash_coins >= 200:
                    st.session_state.crash_coins -= 200
                    st.session_state.cpu_temp = max(20,st.session_state.cpu_temp-40)
                    st.session_state.ram_utilization = max(20,st.session_state.ram_utilization-40)
                    st.session_state.active_bloatware_list = st.session_state.bloatware_list [::2]
                    st.success("the one time nitrogen cooling has been activated")
                    st.session_state.Nitrogen_cooling = True
                    st.rerun()
                else:
                    st.warning("you do not have enough crash coins")

        else:
            st.success("the nitrogen colling has been appilied")
        dificulity = st.select_slider("select_pc_environment",options=["new clean laptop","family pc","thermal throttling nightmare"],value="family pc" )
        if dificulity == "new clean laptop":
            chance_dificulity = 20
            bonus_coin_add = 0.2
        if dificulity =="family pc" :
            chance_dificulity = 10
            bonus_coin_add = 0.5
        if dificulity == "thermal throttling nightmare":
            chance_dificulity = 5
            bonus_coin_add = 1


    if random.randint(1, chance_dificulity) == 1:
        event_choice = random.choice(["win_update", "adware", "fan_fail"])
        if event_choice == "win_update":
            st.warning("windows has forced an update and installed 2 more bloatware")
            spawn()
            spawn()
        elif event_choice == "adware":
            st.warning("adware has been installed by the bloat , causing the cpu temp to spike by 5'c")
            st.session_state.cpu_temp+=5
        elif event_choice == "fan_fail" :
            st.warning("the fan is filling smoke !!!!!. emergency tem spike , reducing cpu clock , increasing ram usage")
            st.session_state.cpu_temp += 7
            st.session_state.ram_utilization += 5

    col1,col2 = st.columns(2)
    with col1:
        st.metric(label="the cpu temp🔥",value=f"{st.session_state.cpu_temp}'c",delta="+2'c")
        st.metric(label="crash coins (cc)",value=f"{st.session_state.crash_coins}")
    with col2:
        st.metric(label="ram utilization ", value=f"{st.session_state.ram_utilization}%", delta="+2'c")
        if st.button("start the game "):
            spawn()


    for i,item in enumerate(st.session_state.active_bloatware_list):
        if isinstance(item,dict):
            app_name = item["name"]
        else:
            app_name = item
        st.warning(f"{app_name} is running and takeing too much powerrrr...")
        c1,c2,c3,c4 =st.columns(4)
        with c1:

            if st.button(f"force kill(taskmanager)",key=f"{i}force_kill",help="this helps with cpu temp but the ram ,not soo much"):
                st.session_state.cpu_temp -= random.randint(2,10 )
                st.session_state.ram_utilization -= random.randint(1,2)
                st.session_state.crash_coins += 1
                st.session_state.active_bloatware_list = [
                app
                for idx,app in enumerate(st.session_state.active_bloatware_list)
                    if idx != i
                ]
                spawn()
                st.rerun()
        with c2:
            if st.button("end task(normal)",key=f"{i}_end_task",help="this helps with the ram utilization , but the tem shoots upp"):
                st.session_state.cpu_temp -= random.randint(2, 4)
                st.session_state.ram_utilization -= random.randint(1, 11)
                st.session_state.crash_coins += 1
                st.session_state.active_bloatware_list = [
                    app
                    for idx, app in enumerate(st.session_state.active_bloatware_list)
                    if idx != i
                    ]
                spawn()
                st.rerun()

        with c3:
            if st.button("use powershell = 10CC",key=f"{i}_powershell",help="this helps both the cpu and ram , but it comes at a cost. 10 crash coins"):
                if st.session_state.crash_coins >= 10:
                    st.session_state.crash_coins -= 10
                    st.session_state.cpu_temp -= random.randint(6, 20)
                    st.session_state.ram_utilization -= random.randint(6 , 18)
                    st.session_state.crash_coins += 1
                    st.session_state.active_bloatware_list = [
                        app
                        for idx, app in enumerate(st.session_state.active_bloatware_list)
                        if idx != i
                    ]
                    spawn()
                    st.rerun()
                else:
                    st.error("you don't have enouch coins")
        with c4:
            if st.button("wait, and do nothing",key=f"{i}_nothing",help="as the name suggests,it does nothing"):
                spawn()
                st.rerun()