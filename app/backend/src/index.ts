import express from "express";
import { API_PATHS } from "shared/dist/constants";
import cors from "cors";
import { Service } from "./services/statis_stock.service";
import Objection from "objection";
import Knex from "knex";
import { PGConnection } from "./constants";

const knex = Knex(PGConnection);
Objection.Model.knex(knex);

const app = express();
const port = 8080; // default port to listen
app.use(
  cors({
    methods: ["GET"],
  })
);

app.get(Service.path, Service.get);

// start the express server
app.listen(port, () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://localhost:${port}`);
});
