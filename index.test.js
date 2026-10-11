import { describe, it, expect } from 'vitest';
import worker from './index.js';

describe('worker fetch handler', () => {
  it('should return Hello World!', async () => {
    const request = new Request('http://localhost');
    const env = {};
    const ctx = {};

    const response = await worker.fetch(request, env, ctx);

    expect(response.status).toBe(200);
    const text = await response.text();
    expect(text).toBe('Hello World!');
  });
});
