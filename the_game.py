import random

import streamlit as st
from streamlit.elements.widgets import button

if "cpu_temp" not in st.session_state:
    st.session_state.cpu_temp = 40
    st.session_state.ram_utilization = 20
    st.session_state.bloatware_list = ["cortona","master chief" ,"ai ","3 mil chrome tabs " , "FH3"]
    st.session_state.active_bloatware_list = []
    st.session_state.apps_running = 0
    st.session_state.crash_coins = 25


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
            st.session_state.crash_coins = 25
            st.session_state.bloatware_list = ["cortona", "master chief", "ai ", "3 mil chrome tabs ", "FH3"]
            st.session_state.active_bloatware_list = []
            st.session_state.apps_running = 0
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
        st.rerun()
else:
    def spawn():
        st.session_state.apps_running += 1
        st.session_state.cpu_temp += random.randint(4,8)
        st.session_state.ram_utilization +=random.randint(3,8)
        app={"name":random.choice(st.session_state.bloatware_list),
             "id":st.session_state.apps_running,
             }
        st.session_state.active_bloatware_list.append(app)


    with st.sidebar:
        st.subheader("STATS")
        st.subheader(f"💥🪙crash coin balance : {st.session_state.crash_coins} ")
        st.subheader(F"deleated bloatware : {st.session_state.apps_running}")
        chance_dificulity = st.slider("chance event frequence(highest dificulty : 5, lowest dificulty : 20)",min_value=5,max_value=20,value=10)
        st.subheader("⌨️ THE SHOP")
        if not st.session_state.get("thermal_paste_apply",False):
            if st.button("buy the thermal paste for 25c(reduces half of cpu temp and ram uti)"):
                if st.session_state.crash_coins >= 25:
                    st.session_state.crash_coins -= 25
                    st.session_state.cpu_temp /=2
                    st.session_state.ram_utilization /=2
                    st.success("the thermal paste has been applied")
                    st.session_state.thermal_paste_apply = True
                    st.rerun()
                else:
                    st.warning("you do not have enough crash coins")
        else:
            st.success("☑️the thermal paste has been applied")
        if not st.session_state.get("dual_fans", False):
            if st.button("buy the thermal paste for 25c(reduces half of cpu temp and ram uti)"):
                if st.session_state.crash_coins >= 25:
                    st.session_state.crash_coins -= 25
                    st.session_state.cpu_temp /= 2
                    st.session_state.ram_utilization /= 2
                    st.success("the dual fans has been applied")
                    st.session_state.dual_fans = True
                    st.rerun()
                else:
                    st.warning("you do not have enough crash coins")
        else:
            st.success("☑️the dual fans has been applied")
        chance_dificulity = st.slider("chance event frequencey(if you don't know how the diffuculty works click the question mark beside the slider)",
                                      min_value=5, max_value=20, value=10,help="lower numbers mean more disasters and higher numbers mean less or rarrer disasters")

    if random.randint(1, chance_dificulity) == 1:
        event_choice = random.choice(["win_update", "adware", "fan_fail"])
        if event_choice == "win_update":
            st.warning("windows has forced an update and installed 3 more bloatware")
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


    for item in st.session_state.active_bloatware_list:

        app_name = item["name"]
        id = item["id"]
        st.warning(f"{app_name} is running and takeing too much powerrrr...")
        c1,c2,c3,c4 =st.columns(4)
        with c1:

            if st.button(f"force kill(taskmanager)",key=f"{id}force_kill"):
                st.session_state.cpu_temp -= random.randint(2,10 )
                st.session_state.ram_utilization -= random.randint(1,2)
                st.session_state.crash_coins += 1
                st.session_state.active_bloatware_list = [
                app for app in st.session_state.active_bloatware_list if id != app["id"]
                ]
                spawn()
                st.rerun()
        with c2:
            if st.button("end task(normal)",key=f"{id}_end_task"):
                st.session_state.cpu_temp -= random.randint(2, 4)
                st.session_state.ram_utilization -= random.randint(1, 11)
                st.session_state.crash_coins += 1
                st.session_state.active_bloatware_list = [
                        app for app in st.session_state.active_bloatware_list if id != app["id"]
                    ]
                spawn()
                st.rerun()

        with c3:
            if st.button("use powershell = 10CC",key=f"{id}_powershell"):
                if st.session_state.crash_coins >= 10:
                    st.session_state.crash_coins -= 10
                    st.session_state.cpu_temp -= random.randint(6, 18)
                    st.session_state.ram_utilization -= random.randint(6 , 18)
                    st.session_state.crash_coins += 1
                    st.session_state.active_bloatware_list = [
                    app for app in st.session_state.active_bloatware_list if id != app["id"]
                    ]
                    spawn()
                    st.rerun()
                else:
                    st.error("you don't have enouch coins")
        with c4:
            if st.button("wait, and do nothing",key=f"{id}_nothing"):
                spawn()
                st.rerun()