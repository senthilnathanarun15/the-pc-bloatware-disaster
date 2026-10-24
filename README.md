# 💾 TaskManager_Sim_95.exe (PC Bloatware Disaster)

A retro **Windows 95-themed simulation game** built with Python and Streamlit. Manage your system resources, fight relentless bloatware, upgrade your cooling hardware, and survive CPU thermal throttling and RAM overloads! this is a game where you play as a user in a computer , deleting bloatware and freeing up resources . there are random events that could tank your performance and in spite of all of this you should keep the computer under control .if not the computer could crash

## 🎮 Gameplay Overview

Your PC is infected with unkillable bloatware applications (`Cortana`, `3 mil Chrome tabs`, `FH3`, etc.). Every action or task spawn pushes your CPU temperature and RAM utilization closer to catastrophic failure (100°C or 100% RAM usage).

Earn **Crash Coins (CC)** by handling tasks and spending them in **The Shop** on PC hardware upgrades to keep your rig alive.

## ✨ Features

* **Retro Windows 95 Visuals:** Custom CSS styling with 3D bevelled buttons, teal desktop background (`#008080`), classic title bars, and retro warning dialogs.

* **Dynamic Resource Management:** Real-time tracking of CPU temperature and RAM utilization.

* **Multiple Task Resolution Methods:**

  * `Force Kill (Task Manager)`: High CPU temp reduction, minimal RAM relief.

  * `End Task (Normal)`: High RAM relief, minimal CPU temp reduction.

  * `Use PowerShell (10 CC)`: Massively cools CPU and frees RAM at the cost of 10 Crash Coins.

  * `Wait, and do nothing`: Lets time pass while spawning more bloatware.

* **Hardware Upgrade Shop:**

  * **Thermal Paste (55 CC):** Reduces CPU temperature buildup per app run.

  * **Dual Fans (80 CC):** Passively mitigates both CPU heat and RAM load.

  * **Liquid Nitrogen Cooling (200 CC):** Emergency one-time use item that slashes CPU temp and RAM usage by 40 units.

* **Dynamic Random Events:** Experience random OS updates, adware spikes, or sudden fan failures.

* **Difficulty Environments:** Choose between *New Clean Laptop*, *Family PC*, and *Thermal Throttling Nightmare*.

## 🚀 Quick Start & Installation

### Prerequisites

* Python 3.8 or higher

* Streamlit

### Installation Steps

1. **Install dependencies:**

   ```
   pip install streamlit
   
   ```

2. **Run the Streamlit application:**

   ```
   streamlit run the_game.py
   
   ```

## 🕹️ Controls & Rules

1. Launch the game using the **"start the game"** button to spawn active bloatware.

2. Select resolution tactics for each running application.

3. Keep an eye on your **CPU Temp** (<100°C) and **RAM Utilization** (<100%).

4. If your system crashes, spend **15 CC** to repair parts or initiate a **Hard Reset** to start fresh.

## 🛠️ Built With

* [**Streamlit**](https://streamlit.io/)**:** Interactive Web Application Framework

* **Python:** Game logic and session state management

* **Custom CSS:** Authentic Windows 95 UI styling
