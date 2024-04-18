#!/bin/sh
echo "one moment..."
sleep 1

script_path=$0
script_dir="$(dirname "$script_path")"

echo "performing environment checks"

echo "running from $script_dir"

echo "checking filesystem..."

mkdir -p "$script_dir"/system/filesystem/opt/main
tar -xf "$script_dir/system/filesystem.tar.gz" --skip-old-files --directory "$script_dir/system/filesystem/"

if ! chmod +x "$script_dir/system/breaker"; then
    echo "[WARN] unable to set permissions properly."
else
    chmod +x "$script_dir/system/breaker"
    echo "[OK] Permissions have been set"
fi

#fix filesystem permissions in some scenario's
chmod +x "$script_dir"/system/filesystem/sbin/apk
#chmod -R 777 "$script_dir"/system/filesystem
chmod -R +x "$script_dir"/system/filesystem

#sleep 1
echo "starting os... (proot)"
#sleep 2

echo "[INFO] updating DNS nameservers (cloudflare)"
echo "nameserver 1.1.1.1" > "$script_dir/system/filesystem/etc/resolv.conf"

echo "[INFO] On some systems, warnings might appear. They can be safely ignored."
#sleep 1

proot_exec() {
    "$script_dir"/system/breaker -r "$script_dir"/system/filesystem -0 $1 2>&1 | grep -v -e 'proot warning' -e 'proot info'
}

echo "[INFO] upgrading basic packages"

proot_exec "/sbin/apk update"
proot_exec "/sbin/apk add python3 bash py3-pip nano openssh sudo openrc"

echo "[INFO] The default packages are installed. entering shell..."

cp "$script_dir"/system/main.py "$script_dir"/system/filesystem/opt/main/main.py

proot_exec "python3 /opt/main/main.py | /bin/bash"