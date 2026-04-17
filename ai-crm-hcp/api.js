const BASE_URL = "http://127.0.0.1:8000";

export const sendInteraction = async (data) => {
  try {
    const response = await fetch(`${BASE_URL}/log`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("API Error");
    }

    return await response.json();
  } catch (error) {
    console.error(error);
    throw error;
  }
};