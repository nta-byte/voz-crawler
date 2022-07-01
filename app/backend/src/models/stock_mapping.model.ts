import { Model, RelationMappings } from "objection";
import { RawComment } from "./raw_comment.model";

export class StockMapping extends Model {
  static get tableName() {
    return "voz_stockmapping";
  }

  static get relationMappings(): RelationMappings {
    return {
      comment: {
        modelClass: RawComment,
        relation: Model.HasOneRelation,
        join: {
          from: this.tableName + ".voz_commentid",
          to: RawComment.tableName + ".id",
        },
      },
    };
  }
}
