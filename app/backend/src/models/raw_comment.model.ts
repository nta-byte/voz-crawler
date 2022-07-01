import { Model } from "objection";

export class RawComment extends Model {
  static get tableName() {
    return "voz_rawcomment";
  }
}
