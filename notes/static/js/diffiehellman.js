// Фронтенд (JavaScript)

async function generateParams() {
    const response = await fetch('/notes/generate_params/', { method: 'POST' });
    const data = await response.json();
    return data;
}

async function sendToBackend(A) {
    const response = await fetch('/notes/calculate_result/', {
        method: 'POST',
        // headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            // 'X-CSRFToken': getCSRFToken(),  // Важно для Django CSRF защиты
        },
        body: `A=${A}`
    });
    const data = await response.json();
    return data.result;
}

// Пример использования
async function performDiffieHellman() {
    const { g, p, b, B } = await generateParams();

    const a = Math.floor(Math.random() * 100) + 1; // Генерация случайного числа от 1 до 100

    const A = (BigInt(g) ** BigInt(a)) % BigInt(p);
    const K_Alice = (BigInt(B) ** BigInt(a)) % BigInt(p);


    const K = (BigInt(g) ** BigInt(a*b)) % BigInt(p);


    // Отправка A на бекенд
    const K_Bob = await sendToBackend(A);

    console.log('Backend - Received g:', g);
    console.log('Backend - Received p:', p);

    console.log('Backend - Received b:', b);
    console.log('Backend - Received B:', B);

    console.log('Frontend - Generated a:', a);
    console.log('Frontend - Generated A:', A.toString());

    console.log('Frontend - K:', K_Alice.toString());
    console.log('Backend - K:', K_Bob);
    console.log('K:', K.toString());
}

// Вызов функции
performDiffieHellman();
