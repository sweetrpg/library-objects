//
// Created by Paul Schifferer on 6/16/21.
//

import Fluent


public extension Studio {
    enum v20210625 {
        // schema
        static let schemaName = "studios"

        // properties
        static let name = FieldKey(stringLiteral: "name")
        static let deletedAt = FieldKey(stringLiteral: "deletedAt")
        static let createdAt = FieldKey(stringLiteral: "createdAt")
        static let updatedAt = FieldKey(stringLiteral: "updatedAt")
    }
}
