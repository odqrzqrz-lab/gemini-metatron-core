export default {
  async fetch(request, env, ctx) {
    return new Response("gemini-metatron-core worker active", {
      headers: { "content-type": "text/plain" },
    });
  },
};
