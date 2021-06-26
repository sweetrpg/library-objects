//
// Created by Paul Schifferer on 6/16/21.
//

import Fluent


public extension System {
    enum v20210625 {
        // schema
        static let schemaName = "systems"

        // properties
        static let gameSystemIdentifier = FieldKey(stringLiteral: "gameSystemIdentifier")
        static let editionIdentifier = FieldKey(stringLiteral: "editionIdentifier")
        static let deletedAt = FieldKey(stringLiteral: "deletedAt")
        static let createdAt = FieldKey(stringLiteral: "createdAt")
        static let updatedAt = FieldKey(stringLiteral: "updatedAt")
    }
}
