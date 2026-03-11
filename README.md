# Network Scanner

Herramienta de análisis de redes desarrollada en Python para detectar dispositivos activos y puertos abiertos dentro de una red local.

## Funciones

- Escaneo de redes LAN
- Identificación de dispositivos activos
- Detección de puertos abiertos
- Exportación automática de reportes JSON
- Configuración mediante argumentos CLI

## Tecnologías

- Python
- Nmap
- Networking
- Linux

## Instalación

Instalar dependencias:

pip install -r requirements.txt

Instalar Nmap:

Linux:

sudo apt install nmap

## Uso

Escaneo básico:

python scanner.py

Escaneo de red específica:

python scanner.py -t 192.168.0.0/24

Escaneo con puertos personalizados:

python scanner.py -t 192.168.0.0/24 -p 22,80,443

## Impacto

Permite analizar la infraestructura de red y detectar dispositivos o servicios expuestos dentro de una red local, facilitando auditorías básicas de seguridad.