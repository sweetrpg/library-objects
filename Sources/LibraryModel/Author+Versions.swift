//
// Author+Version.swift
// Created by Paul Schifferer on 6/16/21.
//

import Fluent


public extension Author {
    enum v20210625 {
        // schema
        static let schemaName = "authors"

        // properties
        static let name = FieldKey(stringLiteral: "name")
        static let deletedAt = FieldKey(stringLiteral: "deletedAt")
        static let createdAt = FieldKey(stringLiteral: "createdAt")
        static let updatedAt = FieldKey(stringLiteral: "updatedAt")
        static let tags = FieldKey(stringLiteral: "tags")
    }
}
