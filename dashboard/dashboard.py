import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

st.header('Bike Sharing Analysis :bike:')
hours_df = pd.read_csv("hour.csv")
days_df = pd.read_csv("day.csv")

st.subheader(":leaves: Jumlah Pesepeda Berdasarkan Musim")
byseason_df = days_df.groupby(by="season").instant.nunique().reset_index()
fig = plt.figure(figsize=(10, 5))
colors = ["#fb6f92", "#ff8fab", "#ffb3c6", "#ffc2d1", "#ffe5ec"]
sns.barplot(
    y="instant",
    x="season",
    data=byseason_df.sort_values(by="instant", ascending=False),
    palette=colors
)

plt.title("Jumlah Pesepeda Berdasarkan Musim", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()
st.pyplot(fig)

st.subheader(":partly_sunny: Jumlah Persebaran Sepeda Berdasarkan Cuaca")
byweather_df = hours_df.groupby(by="weathersit").instant.nunique().reset_index()
byweather_df.rename(columns = {
    "instant" : "biker"
}, inplace = True)
colors = ["#fb6f92", "#ff8fab", "#ffb3c6", "#ffc2d1", "#ffe5ec"]
fig = plt.figure(figsize=(10, 5))

sns.barplot(
    y="biker",
    x="weathersit",
    data=byweather_df.sort_values(by="biker", ascending=False),
    palette=colors
)


plt.title("Jumlah Pesepeda Berdasarkan Cuaca", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()
st.pyplot(fig)

st.subheader(":alarm_clock: Waktu Banyak Pesepeda")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14,6))
colors = ["#fb6f92", "#ff8fab", "#ffb3c6", "#ffc2d1", "#ffe5ec"]
sum_bike_hours_df = hours_df.groupby("hr").cnt.sum().sort_values(ascending=False)
sum_bike_hours_df.head()
if isinstance(sum_bike_hours_df, pd.Series):
    sum_bike_hours_df = sum_bike_hours_df.to_frame()

sns.barplot(x="hr", y="cnt", data=sum_bike_hours_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Waktu Yang Paling Banyak Pengguna", loc="center", fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)

sns.barplot(x="hr", y="cnt", data=sum_bike_hours_df.sort_values(by='cnt', ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].set_title("Waktu Yang Paling Sedikit Pengguna", loc="center", fontsize=15)
st.pyplot(fig)


hour_df = hours_df['hr']
total_biker_df = hours_df['cnt']

hourly_totals = hours_df.groupby(by='hr')[['casual', 'registered']].sum()

hour_df = hourly_totals.index

total_casual_df = hourly_totals['casual']
total_registered_df = hourly_totals['registered']

fig = plt.figure(figsize=(12, 5))
plt.plot(hour_df,total_casual_df, label = 'casual', color='red')
plt.plot(hour_df,total_registered_df, label = 'registered', color='blue')
plt.xlabel('Hour')
plt.xticks(range(0,25))
plt.ylabel('total biker')
plt.title('Total Bikers by Hour')
plt.grid(True)
plt.legend()
plt.show()
st.pyplot(fig)

st.subheader(":star: Perbandingan Jumlah Pesepeda yang Casual dan Registered")
sum_instant_df = ("casual", "registered")
total_instant_df = (days_df.casual.sum(), days_df.registered.sum())
colors = ('#fb6f92', '#ffc2d1')
explode = (0.1, 0)
fig, ax = plt.subplots()
ax.pie(
    x=total_instant_df,
    labels=sum_instant_df,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)
plt.show()
st.pyplot(fig)

