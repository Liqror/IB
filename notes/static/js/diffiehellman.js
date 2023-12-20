// Фронтенд (JavaScript)

const a = Math.floor(Math.random() * 100) + 1; // Генерация случайного числа от 1 до 100
console.log('Frontend - Generated a:', a);

async function generateParams() {
    const response = await fetch('/notes/generate_params/', { method: 'POST' });
    const data = await response.json();
    console.log('Frontend - Received p and g:', data);
    return data;
}

// Пример использования
async function performDiffieHellman() {
    const { p, g } = await generateParams();
    console.log('Frontend - Received p and g:', p);

}

// Вызов функции
performDiffieHellman();
