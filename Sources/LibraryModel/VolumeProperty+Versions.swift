//
// Created by Paul Schifferer on 6/16/21.
//

import Fluent


public extension VolumeProperty {
    enum v20210828 {
        // schema
        static let schemaName = "volume_properties"

        // properties
        static let name = FieldKey(stringLiteral: "name")
        static let type = FieldKey(stringLiteral: "type")
        static let value = FieldKey(stringLiteral: "value")
        static let volumeId = FieldKey(stringLiteral: "volumeId")
        static let deletedAt = FieldKey(stringLiteral: "deletedAt")
        static let createdAt = FieldKey(stringLiteral: "createdAt")
        static let updatedAt = FieldKey(stringLiteral: "updatedAt")
    }
}
