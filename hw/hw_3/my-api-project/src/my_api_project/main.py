import requests


def get_post_title(post_id):
    """Функция для получения заголовка поста по его ID."""
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP-ошибки (4xx или 5xx)

        post_data = response.json()
        print(f"✅ Успех! Заголовок поста #{post_id}:")
        print(post_data["title"])

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка сети или HTTP: {e}")


if __name__ == "__main__":
    get_post_title(1)
