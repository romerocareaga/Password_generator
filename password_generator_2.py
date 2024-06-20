import streamlit as st
import random
import string
import math


def generate_password(platform, user_word):
    # Generar la primera parte de la contraseña: 8 caracteres aleatorios
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    # Asegurarse que la plataforma esté en mayúsculas
    platform_part = platform.upper()
    
    # Combinar todas las partes
    password = random_part + platform_part + user_word
    return password


def calculate_crack_time(password_length_random=8, platform_length=6, user_word_length=8):
    # Entropía de cada parte
    entropy_random = 94**password_length_random
    entropy_platform = 26**platform_length
    entropy_user_word = 26**user_word_length

    # Entropía total (asumiendo que las tres partes son independientes)
    total_entropy = entropy_random * entropy_platform * entropy_user_word

    # Suposición de la tasa de prueba de contraseñas por segundo
    attempts_per_second = 10**12

    # Tiempo estimado en segundos
    time_seconds = total_entropy / attempts_per_second

    # Convertir tiempo en años
    time_years = time_seconds / (60 * 60 * 24 * 365.25)

    return time_years



def main():
    st.title('Generador de Contraseñas Seguras')
    
    platform = st.text_input('Ingresa la plataforma (e.g., Facebook, Gmail)')
    user_word = st.text_input('Ingresa una palabra conocida')

    if st.button('Generar Contraseña'):
        if platform and user_word:
            password = generate_password(platform, user_word)
            crack_time_years = calculate_crack_time(
                password_length_random=8, 
                platform_length=len(platform), 
                user_word_length=len(user_word)
            )
            formatted_time_years = "{:,}".format(int(crack_time_years))
            st.success(f'Tu nueva contraseña es: {password}')
            st.info(f'Tiempo estimado para descifrar la contraseña: {formatted_time_years} años')
        else:
            st.error('Por favor, ingresa ambos valores.')

if __name__ == '__main__':
    main()


