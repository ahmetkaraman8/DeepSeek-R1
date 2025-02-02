def generate_report(name, age):
    with open("report.txt", "a") as f:
        f.write(f"İsim: {name}, Yaş: {age}\n")
    print("Rapor kaydedildi.")