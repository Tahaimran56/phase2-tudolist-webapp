/**
 * API client wrapper with credentials handling for authentication.
 */

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public data?: unknown
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

interface RequestOptions extends RequestInit {
  data?: unknown;
}

async function request<T>(endpoint: string, options: RequestOptions = {}): Promise<T> {
  const { data, ...fetchOptions } = options;

  const config: RequestInit = {
    ...fetchOptions,
    credentials: 'include', // Required for cookies
    headers: {
      'Content-Type': 'application/json',
      ...fetchOptions.headers,
    },
  };

  if (data) {
    config.body = JSON.stringify(data);
  }

  const url = `${API_URL}${endpoint}`;
  console.log('API Request:', { method: config.method, url, data });

  let response;
  try {
    response = await fetch(url, config);
  } catch (error) {
    console.error('Network Error:', { url, error });
    throw new ApiError(
      0,
      'Unable to connect to the server. Please check if the backend is running.',
      { error }
    );
  }

  if (!response.ok) {
    let errorData;
    let errorMessage = 'An error occurred';

    try {
      errorData = await response.json();
      errorMessage = errorData.detail || errorData.message || errorMessage;
    } catch {
      // If we can't parse JSON, use status text
      errorMessage = response.statusText || errorMessage;
      errorData = { detail: errorMessage };
    }

    console.error('API Error:', { status: response.status, url, errorData });
    throw new ApiError(
      response.status,
      errorMessage,
      errorData
    );
  }

  // Handle 204 No Content
  if (response.status === 204) {
    return {} as T;
  }

  return response.json();
}

export const api = {
  get: <T>(endpoint: string, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'GET' }),

  post: <T>(endpoint: string, data?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'POST', data }),

  put: <T>(endpoint: string, data?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'PUT', data }),

  patch: <T>(endpoint: string, data?: unknown, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'PATCH', data }),

  delete: <T>(endpoint: string, options?: RequestOptions) =>
    request<T>(endpoint, { ...options, method: 'DELETE' }),
};
