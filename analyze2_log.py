from datetime import datetime, timedelta

failed_events = []

# janela de tempo: 5 minutos
TIME_WINDOW = timedelta(minutes=5)

with open("sample-log.txt", "r") as file:
    for line in file:
        if "LOGIN FAILED" in line:
            # exemplo de linha:
            # 2026-02-10 09:16:01 LOGIN FAILED user=admin ip=203.0.113.45

            timestamp_str = line.split(" LOGIN")[0]
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            user = line.split("user=")[1].split()[0]
            ip = line.split("ip=")[1].strip()

            failed_events.append({
                "time": timestamp,
                "user": user,
                "ip": ip
            })

print("Tentativas de login com falha (análise por janela de tempo):")

reported = set()

print("Tentativas de login com falha (análise por janela de tempo):")

for i in range(len(failed_events)):
    count = 1
    start_time = failed_events[i]["time"]
    user = failed_events[i]["user"]
    ip = failed_events[i]["ip"]

    key = (user, ip)

    if key in reported:
        continue

    for j in range(i + 1, len(failed_events)):
        if failed_events[j]["time"] - start_time <= TIME_WINDOW:
            if (failed_events[j]["user"] == user and
                failed_events[j]["ip"] == ip):
                count += 1

    if count >= 3:
        print(f"Usuário: {user} | IP: {ip} | Falhas em 5 min: {count}")
        print("⚠ Risco elevado: possível ataque de força bruta\n")
        reported.add(key)
