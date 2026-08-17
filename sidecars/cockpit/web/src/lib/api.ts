export function postJson(url: string, body: unknown) {
  return fetch(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  }).then((res) => {
    window.dispatchEvent(new Event("jarvis-refresh"));
    if (!res.ok) {
      return res.text().then((text) => {
        throw new Error(text.slice(0, 240) || res.statusText);
      });
    }
    return res;
  });
}
