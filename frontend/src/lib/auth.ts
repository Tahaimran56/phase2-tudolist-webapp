/**
 * Authentication utility functions.
 */

import { api, ApiError } from './api';
import type { User, SignupData, SigninData, MessageResponse } from '../types';

export async function signup(data: SignupData): Promise<User> {
  return api.post<User>('/api/auth/signup', data);
}

export async function signin(data: SigninData): Promise<User> {
  return api.post<User>('/api/auth/signin', data);
}

export async function signout(): Promise<MessageResponse> {
  return api.post<MessageResponse>('/api/auth/signout');
}

export async function getCurrentUser(): Promise<User | null> {
  try {
    return await api.get<User>('/api/auth/me');
  } catch (error) {
    if (error instanceof ApiError && error.status === 401) {
      return null;
    }
    throw error;
  }
}

export function isApiError(error: unknown): error is ApiError {
  return error instanceof ApiError;
}
