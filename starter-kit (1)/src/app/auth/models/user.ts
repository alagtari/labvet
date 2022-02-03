import { Role } from './role';

export class User {
  access_token: string;
  status : number;
  token_type : string;
  role: Role;
}
