
# 
```text
 █████╗ ██████╗ ██╗  ██╗     ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗
███████║██████╔╝ ╚███╔╝     ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║
██╔══██║██╔══██╗ ██╔██╗     ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║██╔╝ ██╗    ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
```

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=Matplotlib&logoColor=black)

---

###  ABOUT THE PROJECT

**ARX Casino** is a CLI-based gambling simulation engine built with Python. It features a persistent economy system where user data is stored and retrieved from a local dataset. The application integrates data visualization to track session performance, providing users with a visual representation of their financial trajectory upon exit.

---

###  CORE FEATURES

![User Auth](https://img.shields.io/badge/Authentication-CSV_Database-black?style=flat-square)
> Secure login system validating credentials against a local encrypted-style registry.

![Economy](https://img.shields.io/badge/Economy-Persistent-green?style=flat-square)
> Real-time balance updates saved instantly to `users.csv`. Bankruptcy protection and betting validation included.

![Analytics](https://img.shields.io/badge/Analytics-Matplotlib_Graphs-orange?style=flat-square)
> Automated session graphing. Visualizes your win/loss history with a line graph immediately after the session ends.

---

###  GAME MODES

| GAME | RISK LEVEL | PAYOUT | MECHANIC |
|------|-----------|--------|----------|
| **Lucky Number** | High | **5x** | Random number generation comparison against user input. |
| **Slot Machine** | Medium | **10x - 20x** | Three-reel symbol matching logic. |
| **Roulette** | Variable | **2x - 14x** | Probability-based color prediction (Red/Black/Green). |

---

###  INSTALLATION

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sigma-casino.git
   ```

2. **Install Dependencies**
   ```bash
   pip install numpy pandas matplotlib
   ```

3. **Run the Simulation**
   ```bash
   python casino.py
   ```

---

###  DATA STRUCTURE (`users.csv`)

The system relies on a strictly formatted CSV file for persistence:

```csv
username,password,moeny
admin,admin.123,50000
player1,pass123,1000
```

---

![Status](https://img.shields.io/badge/Status-Active_Development-success?style=for-the-badge)
